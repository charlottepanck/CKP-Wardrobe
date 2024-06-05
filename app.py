from flask import Flask, render_template, redirect, request, session, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import sqlite3
import os

app = Flask(__name__)
DB = 'ckpwardrobe.db'
app.config.from_object(Config)


# Functions
def add_user(table_name, add_name, add_password):
    """Add items to the database."""
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql = f"INSERT INTO {table_name} (username, password) VALUES (?, ?)"
        cursor.execute(sql, (add_name, add_password))
        connection.commit()


def search(username, password):
    """Check if username and password exist in the database."""
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM user WHERE username = ?"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        if user:
            stored_password = user[2]
            if str(password) == str(stored_password):
                print("Password is correct")
                return True, user[0]
            else:
                print(username, stored_password)
                print("Password incorrect")
                return False, None
        else:
            print("User doesn't exist")
            return False, None

@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/user/<int:user_id>")
def get_user_id(user_id):
    if "user_id" in session and session["user_id"] == user_id:
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = ?;", (user_id,))
            user = cursor.fetchone()
        return render_template("user.html", user = user)
    else:
        return redirect(url_for("login"))


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user_authentication, sql_id = search(username, password)
        print(username, password)
        if user_authentication:
            session["user_id"] = sql_id
            print("User authenticated in login function")
            return redirect(url_for("get_user_id", user_id=sql_id))
        else:
            error_message = "Invalid login credentials. Please try again. (Usernames and passwords are case sensitive, spaces also count as cahracters that must be re-entered)"
            return render_template("login.html", error=error_message)
    else:
        if "user_id" in session:
            return redirect(url_for("get_user_id", user_id=session["user_id"]))
        return render_template("login.html")


#@app.route("/logout")
#def logout():
#    session.pop("user_id", None)
#    return redirect(url_for("login"))


@app.route("/add_user")
def add_user_route():
    username = request.args.get('username')
    password = request.args.get('password')
    confirm_password = request.args.get('confirm')
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM user WHERE username = ?;"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        if user and username == user[1]:
            error_message = "Username is taken, please use another name"
            return render_template("signup.html", error_message=error_message)
        if password == confirm_password:
            cursor.execute("INSERT INTO user (username, password) VALUES (?, ?);", (username, password))
            connection.commit()
            return render_template("user.html")
        else:
            error_message = "Your confirmed password is incorrect, please try agaisn"
            return render_template("signup.html", error_message=error_message)


@app.route('/')
def home():
    return render_template('index.html')

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


# view catagories
@app.route('/catagories')
def viewcatagories():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM colour;"
    cursor.execute(sql)
    colour_results = cursor.fetchall()
    sql2 = "SELECT * FROM type;"
    cursor.execute(sql2)
    type_results = cursor.fetchall()
    sql3 = "SELECT * FROM brand;"
    cursor.execute(sql3)
    brands_results = cursor.fetchall()
    db.close()
    return render_template("catagories.html", colour_results=colour_results, type_results=type_results, brands_results=brands_results)


# view outfits
@app.route('/outfits')
def viewoutfits():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT outfit.id, outfit.outfit_id, clothing.name, style.style_name, clothing.img_file
FROM outfit 
LEFT JOIN style ON outfit.outfit_style = style.style_id
LEFT JOIN clothing ON outfit.outfit_img_file = clothing.clothing_id;"""
    cursor.execute(sql)
    outfits_results = cursor.fetchall()
    sql1 = "SELECT clothing_id, name FROM clothing;"
    cursor.execute(sql1)
    resultsclothingo = cursor.fetchall()
    sql2 = "SELECT * FROM style;"
    cursor.execute(sql2)
    resultsstyleo = cursor.fetchall()
    sql3 = "SELECT clothing_id, img_file, name FROM clothing;"
    cursor.execute(sql3)
    resultsimg_fileo = cursor.fetchall()
    db.close()
    return render_template("outfits.html", outfits_results = outfits_results, resultsstyleo=resultsstyleo, resultsclothingo=resultsclothingo, resultsimg_fileo=resultsimg_fileo)


# add clothing
@app.route('/clothing', methods=['GET', 'POST'])
def addclothing():
    if request.method == 'POST':
        name = request.form.get('name')
        brand = request.form.get('brand')
        type = request.form.get('type')
        colour = request.form.get('colour')
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
    
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO clothing (name, brand, type, colour, img_file) VALUES (?, ?, ?, ?, ?);"
            cursor.execute(sql, (name, brand, type, colour, filename))
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
        outfit_id = request.form.get('outfit_id',)
        outfit_style = request.form.get('outfit_style')
        outfit_img_file = request.form.get('outfit_img_file')
        
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO outfit (outfit_id, outfit_style, outfit_img_file) VALUES (?, ?, ?);"
            cursor.execute(sql, (outfit_id, outfit_style, outfit_img_file))
            connection.commit()
            return viewoutfits()
    else:
        return viewoutfits()
    

# add brand
@app.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    if request.method == 'POST':
        brand_name = request.form.get('brand_name')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO brand (brand_name) VALUES (?);"
            cursor.execute(sql, (brand_name,))
            connection.commit()
            return viewcatagories()
    else:
        return viewcatagories()


# add coloue
@app.route('/add_colour', methods=['GET', 'POST'])
def add_colour():
    if request.method == 'POST':
        colour_name = request.form.get('colour_name')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO colour (colour_name) VALUES (?);"
            cursor.execute(sql, (colour_name,))
            connection.commit()
            return viewcatagories()
    else:
        return viewcatagories()


# delete colour
@app.route("/delete_colour/<int:ID>", methods=["POST"])
def delete_colour(ID):
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql_delete = "DELETE FROM colour WHERE colour_id = ?;"
        cursor.execute(sql_delete, (ID,))
        connection.commit()
    return viewcatagories()

# delete type
@app.route("/delete_type/<int:ID>", methods=["POST"])
def delete_type(ID):
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql_delete = "DELETE FROM type WHERE type_id = ?;"
        cursor.execute(sql_delete, (ID,))
        connection.commit()
    return viewcatagories()

# delete brand
@app.route("/delete_brand/<int:ID>", methods=["POST"])
def delete_brand(ID):
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql_delete = "DELETE FROM brand WHERE brand_id = ?;"
        cursor.execute(sql_delete, (ID,))
        connection.commit()
    return viewcatagories()

# add type
@app.route('/add_type', methods=['GET', 'POST'])
def add_type():
    if request.method == 'POST':
        type_name = request.form.get('type_name')

        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO type (type_name) VALUES (?);"
            cursor.execute(sql, (type_name,))
            connection.commit()
            return viewcatagories()
    else:
        return viewcatagories()


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