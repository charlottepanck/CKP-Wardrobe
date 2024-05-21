from flask import Flask, render_template, redirect, request, session, url_for
import sqlite3
app = Flask(__name__)
DB = 'ckpwardrobe.db'


@app.route('/')
def home():
    return render_template('Digital wardrobe.html')

# view clothing
@app.route('/clothing')
def viewclothing():
    # query to find all tops and filter by catagories
    # render poduct page
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT clothing.clothing_id, clothing.name, brand.brand_name, type.type_name, colour.colour_name, clothing.img_file 
FROM clothing 
LEFT JOIN brand on clothing.brand = brand.brand_id
LEFT JOIN type on clothing.type = type.type_id
LEFT JOIN colour on clothing.colour = colour.colour_id
ORDER BY clothing.name;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    sql2 = "SELECT * FROM brand;"
    cursor.execute(sql2)
    resultsbrandsc = cursor.fetchall()
    sql3 = "SELECT * FROM colour;"
    cursor.execute(sql3)
    resultscoloursc = cursor.fetchall()
    sql4 = "SELECT * FROM type;"
    cursor.execute(sql4)
    resultstypec = cursor.fetchall()
    db.close()
    return render_template("clothing.html", results=results, resultsbrandsc=resultsbrandsc, resultstypec=resultstypec, resultscoloursc=resultscoloursc)

# view brands
@app.route('/brands')
def viewbrands():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM brand;"
    cursor.execute(sql)
    brands_results = cursor.fetchall()
    db.close()
    return render_template("brands.html", brands_results=brands_results)

# view clothing types
@app.route('/types')
def viewtypes():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM type;"
    cursor.execute(sql)
    type_results = cursor.fetchall()
    db.close()
    return render_template("types.html", type_results=type_results)

# view colours
@app.route('/colours')
def viewcolours():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM colour;"
    cursor.execute(sql)
    colour_results = cursor.fetchall()
    db.close()
    return render_template("colours.html", colour_results=colour_results)


# vire outfits
@app.route('/outfits')
def viewoutfits():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT outfit.id, outfit.outfit_id, clothing.name, style.style_name, outfit.img_file
FROM outfit 
LEFT JOIN clothing ON outfit.outfit_item = clothing.clothing_id
LEFT JOIN style ON outfit.outfit_style = style.style_id;"""
    cursor.execute(sql)
    outfits_results = cursor.fetchall()
    sql1 = "SELECT clothing_id, name FROM clothing;"
    cursor.execute(sql1)
    resultsclothingo = cursor.fetchall()
    sql2 = "SELECT * FROM style;"
    cursor.execute(sql2)
    resultsstyleo = cursor.fetchall()
    db.close()
    return render_template("outfits.html", outfits_results = outfits_results, resultsstyleo=resultsstyleo, resultsclothingo=resultsclothingo)


# add clothing
@app.route('/clothing', methods=['GET', 'POST'])
def addclothing():
    if request.method == 'POST':
        name = request.form.get('name')
        brand = request.form.get('brand')
        type = request.form.get('type')
        colour = request.form.get('colour')
        img_file = request.form.get('img_file')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO clothing (name, brand, type, colour, img_file) VALUES (?, ?, ?, ?, ?);"
            cursor.execute(sql, (name, brand, type, colour, img_file))
            connection.commit()
            return viewclothing()
    else:
        return viewclothing()
    

# delete clothing
@app.route('/delete_clothing/<int:ID>', methods=['POST'])
def deleteclothing(ID):
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql_delete = "DELETE FROM clothing WHERE clothing_id = ?;"
        cursor.execute(sql_delete, (ID,))
        connection.commit()
    return viewclothing()


# add outfit
@app.route('/outfit', methods=['GET', 'POST'])
def addoutfit():
    if request.method == 'POST':
        outfit_id = request.form.get('outfit_id')
        outfit_item = request.form.get('outfit_item')
        outfit_style = request.form.get('outfit_style')
        img_file = request.form.get('img_file')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO outfit (outfit_id, outfit_item, outfit_style, img_file) VALUES (?, ?, ?, ?);"
            cursor.execute(sql, (outfit_id, outfit_item, outfit_style, img_file))
            connection.commit()
            return viewoutfits()
    else:
        return viewoutfits()
    

# add brand
@app.route('/brands', methods=['GET', 'POST'])
def addbrand():
    if request.method == 'POST':
        brand_name = request.form.get('brand_name')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO brand (brand_name) VALUES (?);"
            cursor.execute(sql, (brand_name,))
            connection.commit()
            return viewbrands()
    else:
        return viewbrands()


# delete outfit
@app.route('/delete_outfit/<int:ID>', methods=['POST'])
def deleteoutfit(ID):
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql_delete = "DELETE FROM outfit WHERE id = ?;"
        cursor.execute(sql_delete, (ID,))
        connection.commit()
    return viewoutfits()


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