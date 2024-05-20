from flask import Flask, render_template, redirect, request, session, url_for
import sqlite3
app = Flask(__name__)
DB = 'ckpwardrobe.db'


@app.route('/')
def home():
    return render_template('Digital wardrobe.html')


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


@app.route('/brands')
def viewbrands():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM brand;"
    cursor.execute(sql)
    brands_results = cursor.fetchall()
    db.close()
    return render_template("brands.html", brands_results=brands_results)


@app.route('/types')
def viewtypes():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM type;"
    cursor.execute(sql)
    type_results = cursor.fetchall()
    db.close()
    return render_template("types.html", type_results=type_results)


@app.route('/colours')
def viewcolours():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM colour;"
    cursor.execute(sql)
    colour_results = cursor.fetchall()
    db.close()
    return render_template("colours.html", colour_results=colour_results)



@app.route('/outfits')
def viewoutfits():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT outfit.outfit_id, clothing.name, style.style_name
FROM outfit 
LEFT JOIN clothing ON outfit.outfit_item = clothing.clothing_id
LEFT JOIN style ON outfit.outfit_style = style.style_name;"""
    cursor.execute(sql)
    outfits_results = cursor.fetchall()
    db.close()
    return render_template("outfits.html", outfits_results = outfits_results)


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