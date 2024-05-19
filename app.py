from flask import Flask, render_template#, redirect, request, session, url_for
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
    sql = """SELECT clothing.clothing_id, clothing.name, brand.brand_name, type.type_name, colour.colour_name 
FROM clothing 
LEFT JOIN brand on clothing.brand = brand.brand_id
LEFT JOIN type on clothing.type = type.type_id
LEFT JOIN colour on clothing.colour = colour.colour_id;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("clothing.html", results = results)#str(results)


@app.route('/outfits')
def viewoutfits():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT outfit.outfit_id, outfit.outfit_name, clothing.name, style.style_name
FROM outfit 
LEFT JOIN clothing on outfit.top = clothing.clothing_id
LEFT JOIN clothing on outfit.bottom = clothing.clothing_id
LEFT JOIN clothing on outfit.outerwear = clothing.clothing_id
LEFT JOIN clothing on outfit.dress = clothing.clothing_id
LEFT JOIN style on outfit.style = style.style_id;"""
    cursor.execute(sql)
    outfits_results = cursor.fetchall()
    db.close()
    return render_template("outfits.html", outfits_results = outfits_results)#str(results)

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