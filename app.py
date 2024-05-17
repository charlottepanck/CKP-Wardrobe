from flask import Flask, render_template, redirect, request, session, url_for
import sqlite3
app = Flask(__name__)
DB = 'ckpwardrobe.db'


@app.route('/')
def home():
    return render_template('Digital wardrobe.html')


# view all brands
@app.route('/brands')
def brands():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql ="SELECT * FROM Brands;"
    cursor.execute(sql)
    resultsbrands = cursor.fetchall()
    db.close()
    return render_template("brands.html", resultsbrands = resultsbrands)


# view all comments
@app.route('/colours')
def colours():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql ="SELECT * FROM Colours;"
    cursor.execute(sql)
    resultscolours = cursor.fetchall()
    db.close()
    return render_template("colours.html", resultscolours=resultscolours)


# view all garments
@app.route('/garments')
def garments():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql ="SELECT * FROM Garments;"
    cursor.execute(sql)
    resultsgarments = cursor.fetchall()
    db.close()
    return render_template("garments.html", resultsgarments=resultsgarments)


# view all styles
@app.route('/styles')
def styles():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql ="SELECT * FROM Styles;"
    cursor.execute(sql)
    resultsstyles = cursor.fetchall()
    db.close()
    return render_template("styles.html", resultsstyles=resultsstyles)


# view all tops & fetch all garments, brands, colours
@app.route('/tops')
def tops():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    sql2 = """SELECT ID, Brand_Name FROM Brands;"""
    cursor.execute(sql2)
    resultsbrandstops = cursor.fetchall()
    sql3 = """SELECT ID, Colour_Type FROM Colours;"""
    cursor.execute(sql3)
    resultscolourstops = cursor.fetchall()
    sql4 = """SELECT ID, Garment_Type FROM Garments;"""
    cursor.execute(sql4)
    resultsgarmentstops = cursor.fetchall()
    db.close()
    return render_template("tops.html", results = results, resultsbrandstops = resultsbrandstops, resultscolourstops = resultscolourstops, resultsgarmentstops = resultsgarmentstops)


# view all bottoms & fetch all garments, brands, colours
@app.route('/bottoms')
def bottoms():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    sql2 = """SELECT ID, Brand_Name FROM Brands;"""
    cursor.execute(sql2)
    resultsbrandsbottoms = cursor.fetchall()
    sql3 = """SELECT ID, Colour_Type FROM Colours;"""
    cursor.execute(sql3)
    resultscoloursbottoms = cursor.fetchall()
    sql4 = """SELECT ID, Garment_Type FROM Garments;"""
    cursor.execute(sql4)
    resultsgarmentsbottoms = cursor.fetchall()
    db.close()
    return render_template("bottoms.html", results1 = results, resultsbrandsbottoms = resultsbrandsbottoms, resultscoloursbottoms = resultscoloursbottoms, resultsgarmentsbottoms = resultsgarmentsbottoms)#str(results)


# view all outerwear & fetch all garments, brands, colours
@app.route('/outerwear')
def outerwear():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    sql2 = """SELECT ID, Brand_Name FROM Brands;"""
    cursor.execute(sql2)
    resultsbrandsouterwear = cursor.fetchall()
    sql3 = """SELECT ID, Colour_Type FROM Colours;"""
    cursor.execute(sql3)
    resultscoloursouterwear = cursor.fetchall()
    sql4 = """SELECT ID, Garment_Type FROM Garments;"""
    cursor.execute(sql4)
    resultsgarmentsouterwear = cursor.fetchall()
    db.close()
    return render_template("outerwear.html", results2 = results, resultsbrandsouterwear = resultsbrandsouterwear, resultscoloursouterwear = resultscoloursouterwear, resultsgarmentsouterwear = resultsgarmentsouterwear)#str(results)


# view all dresses & fetch all garments, brands, colours
@app.route('/dresses')
def dresses():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    sql2 = """SELECT ID, Brand_Name FROM Brands;"""
    cursor.execute(sql2)
    resultsbrandsdresses = cursor.fetchall()
    sql3 = """SELECT ID, Colour_Type FROM Colours;"""
    cursor.execute(sql3)
    resultscoloursdresses = cursor.fetchall()
    sql4 = """SELECT ID, Garment_Type FROM Garments;"""
    cursor.execute(sql4)
    resultsgarmentsdresses = cursor.fetchall()
    db.close()
    return render_template("dresses.html", results3 = results, resultsbrandsdresses = resultsbrandsdresses, resultscoloursdresses = resultscoloursdresses, resultsgarmentsdresses = resultsgarmentsdresses)#str(results)


# view all outfits & fetch all tops, bottoms, outerwear, dresses, styles
@app.route('/outfits')
def outfits():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Outfits.ID, Outfits.Outfit_name, Tops.Name, Bottoms.Name, Outerwear.Name, Dresses.Name, Styles.Style_Name
    FROM Outfits
    LEFT JOIN Tops ON Outfits.Top == Tops.ID
    LEFT JOIN Bottoms ON Outfits.Bottoms == Bottoms.ID
    LEFT JOIN Outerwear ON Outfits.Outerwear == Outerwear.ID
    LEFT JOIN Dresses ON Outfits.Dress == Dresses.ID
    LEFT JOIN Styles ON Outfits.Style == Styles.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    sql2 = """SELECT ID, Name FROM Tops;"""
    cursor.execute(sql2)
    resultstopsoutfits = cursor.fetchall()
    sql3 = """SELECT ID, Name FROM Bottoms;"""
    cursor.execute(sql3)
    resultsbottomsoutfits = cursor.fetchall()
    sql4 = """SELECT ID, Name FROM Outerwear;"""
    cursor.execute(sql4)
    resultsouterwearoutfits = cursor.fetchall()
    sql5 = """SELECT ID, Name FROM Dresses;"""
    cursor.execute(sql5)
    resultsdressesoutfits = cursor.fetchall()
    sql6 = """SELECT ID, Style_Name FROM Styles;"""
    cursor.execute(sql6)
    resultsstylesoutfits = cursor.fetchall()
    db.close()
    return render_template("outfits.html", results4=results, resultstopsoutfits=resultstopsoutfits, resultsbottomsoutfits=resultsbottomsoutfits, resultsouterwearoutfits=resultsouterwearoutfits, resultsdressesoutfits=resultsdressesoutfits, resultsstylesoutfits=resultsstylesoutfits)#str(results)


# add top
@app.route('/tops', methods = ['GET', 'POST'])
def addtops():
    if request.method == 'POST':
        name = request.form.get('name')
        brand = request.form.get('brand')
        colour = request.form.get('colour')
        garment = request.form.get('garment')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Tops (name, brand, colour, garment) VALUES (?, ?, ?, ?);"
            cursor.execute(sql, (name, brand, colour, garment))
            connection.commit()
            return tops() #render_template('tops.html')
            
    else:
        return tops() #render_template('tops.html')


# add bottom
@app.route('/bottoms', methods = ['GET', 'POST'])
def addbottoms():
    if request.method == 'POST':
        name = request.form.get('name')
        brand = request.form.get('brand')
        colour = request.form.get('colour')
        garment = request.form.get('garment')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Bottoms (name, brand, colour, garment) VALUES (?, ?, ?, ?);"
            cursor.execute(sql, (name, brand, colour, garment))
            connection.commit()
            return bottoms() #render_template('addbottoms.html')
    else:
        return bottoms() #render_template('addbottoms.html')


# add outerwear
@app.route('/outerwear', methods = ['GET', 'POST'])
def addouterwear():
    if request.method == 'POST':
        name = request.form.get('name')
        brand = request.form.get('brand')
        colour = request.form.get('colour')
        garment = request.form.get('garment')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Outerwear (name, brand, colour, garment) VALUES (?, ?, ?, ?);"
            cursor.execute(sql, (name, brand, colour, garment))
            connection.commit()
            return outerwear() #render_template('addouterwear.html')
    else:
        return outerwear() #render_template('addouterwear.html')


# add dress
@app.route('/dresses', methods = ['GET', 'POST'])
def adddresses():
    if request.method == 'POST':
        name = request.form.get('name')
        brand = request.form.get('brand')
        colour = request.form.get('colour')
        garment = request.form.get('garment')
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Dresses (name, brand, colour, garment) VALUES (?, ?, ?, ?);"
            cursor.execute(sql, (name, brand, colour, garment))
            connection.commit()
            return dresses()
    else:
        return dresses()


# add outfit
@app.route('/outfits', methods = ['GET', 'POST'])
def addoutfits():
    if request.method == 'POST':
        outfit_name = request.form.get('outfit_name')
        top = request.form.get('top')
        bottoms = request.form.get('bottoms')
        outerwear = request.form.get('outerwear')
        dress = request.form.get('dress')
        style = request.form.get('style')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Outfits (outfit_name, top, bottoms, outerwear, dress, style) VALUES (?, ?, ?, ?, ?, ?);"
            cursor.execute(sql, (outfit_name, top, bottoms, outerwear, dress, style))
            connection.commit()
            return outfits() #render_template('addoutfits.html')
    else:
        return outfits() #render_template('addoutfits.html')


# add brands
@app.route('/brands', methods = ['GET', 'POST'])
def addbrands():
    if request.method == 'POST':
        brand_name = request.form.get('brand_name')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Brands (brand_name) VALUES (?);"
            cursor.execute(sql, (brand_name,))
            connection.commit()
            return brands()
    else:
        return brands()


# add colours
@app.route('/colours', methods = ['GET', 'POST'])
def addcolours():
    if request.method == 'POST':
        colour_type = request.form.get('colour_type')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Colours (colour_type) VALUES (?);"
            cursor.execute(sql, (colour_type,))
            connection.commit()
            return colours()
    else:
        return colours()


# add garments
@app.route('/garments', methods = ['GET', 'POST'])
def addgarments():
    if request.method == 'POST':
        garment_type = request.form.get('garment_type')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Garments (garment_type) VALUES (?);"
            cursor.execute(sql, (garment_type,))
            connection.commit()
            return garments()
    else:
        return garments()


# add styles
@app.route('/styles', methods = ['GET', 'POST'])
def addstyles():
    if request.method == 'POST':
        style_name = request.form.get('style_name')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Styles (style_name) VALUES (?);"
            cursor.execute(sql, (style_name,))
            connection.commit()
            return styles()
    else:
        return styles()
    

# delete top
@app.route('/delete_top/<int:ID>', methods=['POST'])
def delete_top(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Tops WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return tops()


# delete bottom
@app.route('/delete_bottom/<int:ID>', methods=['POST'])
def delete_bottom(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Bottoms WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return bottoms()


# delete outerwear
@app.route('/delete_outerwear/<int:ID>', methods=['POST'])
def delete_outerwear(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Outerwear WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return outerwear()


# delete dress
@app.route('/delete_dresses/<int:ID>', methods=['POST'])
def delete_dresses(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Dresses WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return dresses()


# delete outfit
@app.route('/delete_outft/<int:ID>', methods=['POST'])
def delete_outfit(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Outfits WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return outfits()

# delete brand
@app.route("/delete_brand/<int:ID>", methods=["POST"])
def delete_brand(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Brands WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return brands()


# delete colour
@app.route("/delete_colour/<int:ID>", methods=["POST"])
def delete_colour(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Colours WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return colours()


# delete garment
@app.route("/delete_garment/<int:ID>", methods=["POST"])
def delete_garment(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Garments WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return garments()


# delete style
@app.route("/delete_style/<int:ID>", methods=["POST"])
def delete_style(ID):
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM Styles WHERE ID = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return styles()

# edit top
#@app.route('/edit_top/<int:ID>', methods=['POST'])
#def edit_top(ID):
#    if request.method == 'POST':
#        Name = request.form.get('Name')
#        brand = request.form.get('brand')
#        colour = request.form.get('colour')
#        garment = request.form.get('garment')

#        with sqlite3.connect(DB) as connection:
#            cursor = connection.cursor()
#            sql_edit = "UPDATE Tops SET Name = ?, brand = ?, colour = ?, garment = ? WHERE ID = ?;"
#            cursor.execute(sql_edit, (Name, brand, colour, garment, ID))
#            connection.commit()
#            return tops()
#    else:
#        return tops()


# page not fount error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error='Page not found, Please check that the Web site address is spelled correctly.'), 404


# internal server error 
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error='Internal server error'), 500


# somthing else error
#@app.errorhandler(Exception)
#def unexpected_error(error):
#    return render_template('error.html', error='Something went wrong'), 500


if __name__ == "__main__":
    app.run(debug=True)