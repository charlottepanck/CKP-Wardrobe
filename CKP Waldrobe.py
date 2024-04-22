import sqlite3

DB = 'ckpwaldrobe.db'
def checkbrandidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Brands WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid
    
def checkcolouridisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Colours WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid


def checkgarmentidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Garments WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid


def fetchallclothes():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Clothes.ID, Clothes.Name, Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close

def fetchallbrands():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Brands;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close

def fetchallgarments():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Garments;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close


def fetchcolours():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Colours;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close


def fetchclothesbycolour(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""SELECT Clothes.ID, Clothes.Name, Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID
    WHERE Clothes.Colour == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close

def fetchclothesbybrand(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""SELECT Clothes.ID, Clothes.Name, Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID
    WHERE Clothes.Brand == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close


def fetchclothesbygarment(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""SELECT Clothes.ID, Clothes.Name, Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID
    WHERE Clothes.Garment == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)
    db.close

print("Charlotte's Digital Waldrobe <3")
while True:
    userinput = input("""
    Enter 'a' to view all clothes
    Enter 'b' to view all brands
    Enter 'c' to view all garment types
    Enter 'exit' to exit program
    >>> """).lower()
    if userinput == 'a':
        fetchallclothes()
        while True:
            userinput1 = input("""
    Enter 'a' to show clothes filtered by colour
    Enter 'b' to show clothes filtered by brand
    Enter 'c' to show clothes filtered by garment type
    Enter 'x' to go back
    >>> """).lower()
            if userinput1 == 'a':
                fetchcolours()
                while True:
                    id = input("\nEnter Colour ID: ")
                    if id.isnumeric() == True:
                        if checkcolouridisvalid(id) == True:
                            fetchclothesbycolour(id)
                            break
                        if checkcolouridisvalid(id) == False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() == False:
                        print("\nInvalid Input!\nID must be an Integer.\nTry Again...")
            if userinput1 == 'b':
                fetchallbrands()
                while True:
                    id = input("\nEnter Brand ID: ")
                    if id.isnumeric() == True:
                        if checkbrandidisvalid(id) == True:
                            fetchclothesbybrand(id)
                            break
                        if checkbrandidisvalid(id) == False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() == False:
                        print("\nInvalid Input!\nId must be an Integer.\nTry Again...")
            if userinput1 == 'c':
                fetchallgarments()
                while True:
                    id = input("\nEnter Garment ID: ")
                    if id.isnumeric() == True:
                        if checkgarmentidisvalid(id) == True:
                            fetchclothesbygarment(id)
                            break
                        if checkgarmentidisvalid(id) == False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() == False:
                        print("\nInvalid Input!\nID must be an Integer.\nTry Again...")
            if userinput1 == 'x':
                break
    if userinput == 'b':
        fetchallbrands()
    if userinput == 'c':
        fetchallgarments()
    if userinput == 'exit':
        break