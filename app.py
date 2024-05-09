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
    sql = """SELECT Outfits.ID, Tops.Name, Bottoms.Name, Outerwear.Name, Dresses.Name, Styles.Style_Name
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


@app.route('/addtops')
def addtops():
    #db = sqlite3.connect(DB)
    #cursor = db.cursor()
    #sql = "INSERT INTO Tops (Name, Brand, Colour, Garment) VALUES ("{name}", "{brand}", "{colour}", "{garment}");"
    #cursor.execute(sql)
    #results = cursor.fetchall()
    #db.close()
    return render_template('addtops.html')


@app.route('/removetops')
def removetops():
    return render_template('removetops.html')
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


if __name__ == "__main__":
    app.run(debug=True)