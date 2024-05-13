from flask import Flask, render_template, redirect, request, session, url_for
import sqlite3
app = Flask(__name__)
DB = 'ckpwardrobe.db'


@app.route('/')
def home():
    return render_template('Digital wardrobe.html')


@app.route('/tops')
def tops():
    # query to find all tops and filter by catagories
    # render poduct page
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID
    WHERE Tops.Name != 'N/A';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("tops.html", results = results)#str(results)


@app.route('/bottoms')
def bottoms():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID
    WHERE Bottoms.Name != 'N/A';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("bottoms.html", results1 = results)#str(results)


@app.route('/outerwear')
def outerwear():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID
    WHERE Outerwear.Name != 'N/A';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("outerwear.html", results2 = results)#str(results)


@app.route('/dresses')
def dresses():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID
    WHERE Dresses.Name != 'N/A';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("dresses.html", results3 = results)#str(results)


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
    db.close()
    return render_template("outfits.html", results4 = results)#str(results)


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


@app.route('/adddresses', methods = ['GET', 'POST'])
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
            return dresses() #render_template('adddresses.html')
    else:
        return dresses() #render_template('adddresses.html')


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


@app.route('/removetops')
def removetops():
    if request.method == 'POST':
        top_id = request.form.get('top_id')
        with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                sql = "DELETE FROM Tops WHERE ID = ?;"
                cursor.execute(sql, top_id)
                connection.commit()
                return render_template('addoutfits.html')
    else:
        return render_template('removetops.html')


if __name__ == "__main__":
    app.run(debug=True)