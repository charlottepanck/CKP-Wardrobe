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


def addclothigitem(name, brand, colour, garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'INSERT INTO Clothes (Name, Brand, Colour, Garment) VALUES ("{name}", "{brand}", "{colour}", "{garment}");'
    cursor.execute(sql)
    db.commit()


def addbrand(brand):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'INSERT INTO Brands (Brand_Name) VALUES ("{brand}");'
    cursor.execute(sql)
    db.commit()


def addgarment(garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'INSERT INTO Garments (Garment) VALUES ("{garment}");'
    cursor.execute(sql)
    db.commit()


def addcolour(colour):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'INSERT INTO Colours (Colour) VALUES ("{colour}");'
    cursor.execute(sql)
    db.commit()


print("Charlotte's Digital Waldrobe <3")
while True:
    userinput = input("""
    Enter 'a' to view all clothes
    Enter 'b' to view all brands
    Enter 'c' to view all garment types
    Enter 'd' to add a clothing item
    Enter 'e' to add a brand
    Enter 'f' to add a garment type
    Enter 'g' to add a color
    Enter 'h' to remove a clothing item
    Enter 'exit' to exit program
    Enter 'x' at any point of the program to go back :)
    >>> """).lower()
    if userinput == 'a':
        fetchallclothes()
        while True:
            userinput1 = input("""
    Enter 'a' to show clothes filtered by colour
    Enter 'b' to show clothes filtered by brand
    Enter 'c' to show clothes filtered by garment type
    >>> """).lower()
            if userinput1 == 'a':
                fetchcolours()
                while True:
                    id = input("\nEnter Colour ID: ")
                    if id == 'x' or id == 'X':
                        break
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
                    if id == 'x' or id == 'X':
                        break
                    if id.isnumeric() == True:
                        if checkbrandidisvalid(id) == True:
                            fetchclothesbybrand(id)
                            break
                        if checkbrandidisvalid(id) == False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() == False:
                        print("\nInvalid Input!\nID must be an Integer.\nTry Again...")
            if userinput1 == 'c':
                fetchallgarments()
                while True:
                    id = input("\nEnter Garment ID: ")
                    if id == 'x' or id == 'X':
                        break
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
    if userinput == 'd':
        flag = False
        while True:
            if flag == True:
                break
            name = input("Name: ").title()
            if name == 'x' or name == 'X':
                break
            fetchallbrands()
            while True:
                if flag == True:
                    break
                brand = input("Brand ID: ").lower()
                if brand == 'x':
                    flag = True
                elif brand.isnumeric() == False:
                    print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                elif brand.isnumeric() == True:
                    if checkbrandidisvalid(brand) == False:
                        print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                    if checkbrandidisvalid(brand) == True:
                        fetchcolours()
                        while True:
                            if flag == True:
                                break
                            colour = input("Colour ID: ").lower()
                            if colour == 'x':
                                flag = True
                            elif colour.isnumeric() == False:
                                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                            elif colour.isnumeric() == True:
                                if checkcolouridisvalid(colour) == False:
                                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                if checkcolouridisvalid(colour) == True:
                                    fetchallgarments()
                                    while True:
                                        if flag == True:
                                            break
                                        garment = input("Garment ID: ").lower()
                                        if garment == 'x':
                                            flag = True
                                        elif garment.isnumeric() == False:
                                            print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                                        elif garment.isnumeric() == True:
                                            if checkgarmentidisvalid(garment) == False:
                                                print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                            if checkgarmentidisvalid(garment) == True:
                                                addclothigitem(name, brand, colour, garment)
                                                flag = True
                                                break
    if userinput == 'e':
        fetchallbrands()
        brand = input("Enter New Brand Name: ").title()
        addbrand(brand)
    if userinput == 'f':
        fetchallgarments()
        garment = input("Enter New Garment Type: ").title()
        addgarment(garment)
    if userinput == 'g':
        fetchcolours()
        colour = input("Enter New Colour: ").title()
        addcolour(colour)
    if userinput == 'h':
        fetchallclothes()
        print("Remove clothing here")
    if userinput == 'exit' or userinput == 'x':
        break