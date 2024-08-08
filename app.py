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
        #add user name and password to database
        sql = f"INSERT INTO {table_name} (username, password) VALUES (?, ?);"
        cursor.execute(sql, (add_name, add_password))
        connection.commit()


def search(username, password):
    """check if username and password exist in the database"""
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM user WHERE username = ?"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        # check if entered password is correct
        if user:
            stored_password = user[2]
            if check_password_hash(str(stored_password), str(password)): #str(password) == str(stored_password):
                print("Password is correct")
                return True, user[0]
            else:
                print(username, stored_password)
                print("Password incorrect")
                return False, None
        # if user doesn't exist
        else:
            print("User doesn't exist")
            return False, None


@app.route("/index/<int:user_id>")
def get_user_id(user_id):
    """fetch user id"""
    if "user_id" in session and session["user_id"] == user_id:
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = ?;", (user_id,))
            user = cursor.fetchall()
        return render_template("index.html", user=user)
    else:
        return redirect(url_for("login"))


@app.route('/')
def home():
    """route to login when site loads"""
    return render_template('login.html')


@app.route("/signup")
def signup():
    """load sign up form"""
    return render_template('signup.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    """Log user in"""
    # get data from form
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # check if username and password exist in the database
        user_authentication, sql_id = search(username, password)
        print(username, password)
        if user_authentication:
            session["user_id"] = sql_id
            print("User authenticated in login function")
            return redirect(url_for("get_user_id", user_id=sql_id))
        # username or password dont match database
        else:
            error_message = "Invalid login credentials. Please try again."
            return render_template("login.html", error_message=error_message)
    else:
        #user logged in
        if "user_id" in session:
            return redirect(url_for("get_user_id", user_id=session["user_id"]))
        return render_template("login.html")


@app.route("/logout")
def logout():
    """log user out"""
    session.pop("user_id", None)
    #return to login page
    return redirect(url_for("login"))


@app.route("/add_user")
def add_user_route():
    """add user to database"""
    #get data from form
    username = request.args.get('username')
    password = request.args.get('password')
    confirm_password = request.args.get('confirm')
    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM user WHERE username = ?"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        #check username isn't taken
        if user and username == user[1]:
            error_message = "Username is taken, please use another name"
            return render_template("signup.html", title="Sign up", error_message=error_message)
        #check passwords match
        if password == confirm_password:
            hashed = generate_password_hash(password)
            cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hashed))
            connection.commit()
            return render_template("login.html")
        else:
            error_message = "Passwords don't match"
            return render_template("signup.html", title="Sign up", error_message=error_message)


# view clothing
@app.route('/clothing/<int:user_id>')
def viewclothing(user_id):
    """View clothing"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        db = sqlite3.connect(DB)
        cursor = db.cursor()
        # select data from database
        cursor.execute("""SELECT clothing.clothing_id, clothing.name, brand.brand_name, type.type_name, colour.colour_name, clothing.img_file, clothing.user_id
FROM clothing
LEFT JOIN brand on clothing.brand = brand.brand_id
LEFT JOIN type on clothing.type = type.type_id
LEFT JOIN colour on clothing.colour = colour.colour_id
WHERE clothing.user_id = ?;""", (user_id,))
        results = cursor.fetchall()

        cursor.execute("""SELECT clothing.clothing_id, clothing.name, brand.brand_name, type.type_name, colour.colour_name, clothing.img_file, clothing.user_id
FROM clothing
LEFT JOIN brand on clothing.brand = brand.brand_id
LEFT JOIN type on clothing.type = type.type_id
LEFT JOIN colour on clothing.colour = colour.colour_id
WHERE clothing.user_id = ?;""", (user_id,))
        two_results = cursor.fetchall()

        cursor.execute("SELECT * FROM brand WHERE user_id =?", (user_id,))
        resultsbrandsc = cursor.fetchall()

        cursor.execute("SELECT * FROM colour WHERE user_id =?", (user_id,))
        resultscoloursc = cursor.fetchall()

        cursor.execute("SELECT * FROM type WHERE user_id =?", (user_id,))
        resultstypec = cursor.fetchall()

        db.close()
        return render_template("clothing.html", user_id=user_id, results=results, two_results=two_results, resultsbrandsc=resultsbrandsc, resultstypec=resultstypec, resultscoloursc=resultscoloursc)
    else:
        return redirect(url_for('login'))


# view brands
@app.route('/brands/<int:user_id>')
def viewbrands(user_id):
    """View brands"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        db = sqlite3.connect(DB)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM brand WHERE user_id =?", (user_id,))
        brands_results = cursor.fetchall()
        db.close()
        return render_template("brands.html", user_id=user_id, brands_results=brands_results)
    else:
        return redirect(url_for('login'))


# view styles
@app.route('/styles/<int:user_id>')
def viewstyles(user_id):
    """view styles"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        db = sqlite3.connect(DB)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM style WHERE user_id =?", (user_id,))
        styles_results = cursor.fetchall()
        db.close()
        return render_template("styles.html", user_id=user_id, styles_results=styles_results)
    else:
        return redirect(url_for('login'))


# view types
@app.route('/types/<int:user_id>')
def viewtypes(user_id):
    """view types"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        db = sqlite3.connect(DB)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM type WHERE user_id =?", (user_id,))
        types_results = cursor.fetchall()
        db.close()
        return render_template("types.html", user_id=user_id, types_results=types_results)
    else:
        return redirect(url_for('login'))


# view colours
@app.route('/colours/<int:user_id>')
def viewcolours(user_id):
    """view colours"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        db = sqlite3.connect(DB)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM colour WHERE user_id =?", (user_id,))
        colours_results = cursor.fetchall()
        db.close()
        return render_template("colours.html", user_id=user_id, colours_results=colours_results)
    else:
        return redirect(url_for('login'))


# view outfits
@app.route('/outfits/<int:user_id>')
def viewoutfits(user_id):
    """view outfits"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        db = sqlite3.connect(DB)
        cursor = db.cursor()
        # get data from database
        cursor.execute("""SELECT outfit.id, outfit.outfit_id, clothing.name, style.style_name, clothing.img_file, outfit.user_id
    FROM outfit
    LEFT JOIN style ON outfit.outfit_style = style.style_id
    LEFT JOIN clothing ON outfit.outfit_img_file = clothing.clothing_id
    WHERE outfit.user_id=?;""", (user_id,))
        outfits_results = cursor.fetchall()
        cursor.execute("""SELECT outfit.id, outfit.outfit_id, clothing.name, style.style_name, clothing.img_file, outfit.user_id
    FROM outfit
    LEFT JOIN style ON outfit.outfit_style = style.style_id
    LEFT JOIN clothing ON outfit.outfit_img_file = clothing.clothing_id
    WHERE outfit.user_id=?
    GROUP BY outfit.outfit_id;""", (user_id,))
        new_outfits_results = cursor.fetchall()
        cursor.execute("SELECT clothing_id, name FROM clothing WHERE user_id=?;", (user_id,))
        resultsclothingo = cursor.fetchall()
        cursor.execute("SELECT * FROM style WHERE user_id=?;", (user_id,))
        resultsstyleo = cursor.fetchall()
        cursor.execute("SELECT clothing_id, img_file, name FROM clothing WHERE user_id=?;", (user_id,))
        resultsimg_fileo = cursor.fetchall()
        db.close()
        return render_template("outfits.html", user_id=user_id, new_outfits_results=new_outfits_results, outfits_results=outfits_results, resultsstyleo=resultsstyleo, resultsclothingo=resultsclothingo, resultsimg_fileo=resultsimg_fileo)
    else:
        return redirect(url_for('login'))


# add clothing
@app.route('/clothing', methods=['GET', 'POST'])
def addclothing():
    """add clothing"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            # get data from user form
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
            # add new data to database
            with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                sql = "INSERT INTO clothing (name, brand, type, colour, img_file, user_id) VALUES (?, ?, ?, ?, ?, ?);"
                cursor.execute(sql, (name, brand, type, colour, filename, user_id))
                connection.commit()
            # return redirect(url_for('get_user_id', user_id=user_id))
            return viewclothing(user_id)
        return viewclothing(user_id)
    else:
        return redirect(url_for('login'))


# delete clothing
@app.route('/delete_clothing/<int:ID>', methods=['POST'])
def deleteclothing(ID):
    """delete clothing"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            sql_delete = "DELETE FROM clothing WHERE clothing_id = ? and user_id = ?;"
            cursor.execute(sql_delete, (ID, user_id))
            connection.commit()
        return viewclothing(user_id)


# add outfit
@app.route('/outfits', methods=['GET', 'POST'])
def addoutfit():
    """add outfit"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            # get data from user from form
            outfit_id = request.form.get('outfit_id',)
            outfit_style = request.form.get('outfit_style')
            outfit_img_file = request.form.get('outfit_img_file')

            with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                # add data to database
                sql = "INSERT INTO outfit (outfit_id, outfit_style, outfit_img_file, user_id) VALUES (?, ?, ?, ?);"
                cursor.execute(sql, (outfit_id, outfit_style, outfit_img_file, user_id))
                connection.commit()
            return viewoutfits(user_id)
        return viewoutfits(user_id)
    else:
        return redirect(url_for('login'))


# add brand
@app.route('/brands', methods=['GET', 'POST'])
def add_brand():
    """add brand"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            #get data from form
            brand_name = request.form.get('brand_name')

            with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                # add data to database
                sql = "INSERT INTO brand (brand_name, user_id) VALUES (?, ?);"
                cursor.execute(sql, (brand_name, user_id))
                connection.commit()
            return viewbrands(user_id)
        return viewbrands(user_id)
    else:
        return redirect(url_for('login'))


# add brand
@app.route('/styles', methods=['GET', 'POST'])
def add_style():
    """add style"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            # get data from form
            style_name = request.form.get('style_name')

            with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                # add data to database
                sql = "INSERT INTO style (style_name, user_id) VALUES (?, ?);"
                cursor.execute(sql, (style_name, user_id))
                connection.commit()
            return viewstyles(user_id)
        return viewstyles(user_id)
    else:
        return redirect(url_for('login'))


# add colour
@app.route('/colours', methods=['GET', 'POST'])
def add_colour():
    """add colour"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            # get data from form
            colour_name = request.form.get('colour_name')

            with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                # add data to database
                sql = "INSERT INTO colour (colour_name, user_id) VALUES (?, ?);"
                cursor.execute(sql, (colour_name, user_id))
                connection.commit()
            return viewcolours(user_id)
        return viewcolours(user_id)
    else:
        return redirect(url_for('login'))


# add type
@app.route('/types', methods=['GET', 'POST'])
def add_type():
    """add type"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            # get data from form
            type_name = request.form.get('type_name')

            with sqlite3.connect(DB) as connection:
                cursor = connection.cursor()
                # add data to database
                sql = "INSERT INTO type (type_name, user_id) VALUES (?, ?);"
                cursor.execute(sql, (type_name, user_id))
                connection.commit()
            return viewtypes(user_id)
        return viewtypes(user_id)
    else:
        return redirect(url_for('login'))


# delete style
@app.route("/delete_style/<int:ID>", methods=["POST"])
def delete_style(ID):
    """delete style"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            #delete data from database
            sql_delete = "DELETE FROM style WHERE style_id = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return viewstyles(user_id)
    else:
        return redirect(url_for('login'))


# delete colour
@app.route("/delete_colour/<int:ID>", methods=["POST"])
def delete_colour(ID):
    """delete colour"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            #delete database
            sql_delete = "DELETE FROM colour WHERE colour_id = ? and user_id = ?;"
            cursor.execute(sql_delete, (ID, user_id))
            connection.commit()
        return viewcolours(user_id)
    else:
        return redirect(url_for('login'))


# delete type
@app.route("/delete_type/<int:ID>", methods=["POST"])
def delete_type(ID):
    """delete type"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            #delete data from database
            sql_delete = "DELETE FROM type WHERE type_id = ? and user_id = ?;"
            cursor.execute(sql_delete, (ID, user_id))
            connection.commit()
        return viewtypes(user_id)
    else:
        return redirect(url_for('login'))


# delete brand
@app.route("/delete_brand/<int:ID>", methods=["POST"])
def delete_brand(ID):
    """delete brand"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            # delete data from database
            sql_delete = "DELETE FROM brand WHERE brand_id = ? and user_id = ?;"
            cursor.execute(sql_delete, (ID, user_id))
            connection.commit()
        return viewbrands(user_id)
    else:
        return redirect(url_for('login'))


# delete outfit
@app.route('/delete_outfit/<int:ID>', methods=['POST'])
def deleteoutfit(ID):
    """delete outfit"""
    #check user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        with sqlite3.connect(DB) as connection:
            cursor = connection.cursor()
            # delete data from database
            sql_delete = "DELETE FROM outfit WHERE id = ?;"
            cursor.execute(sql_delete, (ID,))
            connection.commit()
        return viewoutfits(user_id)


@app.errorhandler(404)
def page_not_found(error):
    """page not fount error"""
    return render_template('error.html', error='Page not found, Please check that the Web site address is spelled correctly.'), 404


@app.errorhandler(500)
def internal_server_error(error):
    """internal server error"""
    return render_template('error.html', error='Internal server error'), 500


@app.errorhandler(Exception)
def unexpected_error(error):
    """somthing else error"""
    return render_template('error.html', error='Something went wrong'), 500


if __name__ == "__main__":
    app.run(debug=True)
