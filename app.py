from flask import Flask, render_template
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
    LEFT JOIN Colours ON Tops.Colour = Colours.ID;"""
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
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("bottoms.html", results = results)#str(results)

if __name__ == "__main__":
    app.run(debug=True)