import sqlite3

DB = 'ckpwaldrobe.db'


def checkclothingidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Clothes WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid


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
    print("ID | Brand")
    for i in results:
        print(f"{i[0]:2} | {i[1]}")
    db.close


def fetchallgarments():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Garments;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("ID | Garment")
    for i in results:
        print(f"{i[0]:2} | {i[1]}")
    db.close


def fetchcolours():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Colours;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("ID | Colour")
    for i in results:
        print(f"{i[0]:2} | {i[1]}")
    db.close


def fetchallclothes():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = """SELECT Clothes.ID, Clothes.Name,
    Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print("ID | Name | Brand | Colour | Garment")
    for i in results:
        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} ")
    db.close


def fetchclothesbycolour(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""SELECT Clothes.ID, Clothes.Name,
    Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID
    WHERE Clothes.Colour == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print("ID | Name | Brand | Colour | Garment")
    for i in results:
        print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} ")
    db.close

def fetchclothesbybrand(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # name column format
    sql1 = """SELECT Name FROM Clothes
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        nlg = len(x)
        nsp = (nlg-4) * " "
    # brand column format
    sql2 = """SELECT Brand_Name FROM Brands
    ORDER BY Length(Brand_Name) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        blg = len(x)
        bsp = (blg-5) * " "
    # colour column format
    sql3 = """SELECT Colour FROM Colours
    ORDER BY Length(Colour) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment FROM Garments
    ORDER BY Length(Garment) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    sql = f"""SELECT Clothes.ID, Clothes.Name,
    Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID
    WHERE Clothes.Brand == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {nsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{nlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchclothesbygarment(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # name column format
    sql1 = """SELECT Name FROM Clothes
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        nlg = len(x)
        nsp = (nlg-4) * " "
    # brand column format
    sql2 = """SELECT Brand_Name FROM Brands
    ORDER BY Length(Brand_Name) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        blg = len(x)
        bsp = (blg-5) * " "
    # colour column format
    sql3 = """SELECT Colour FROM Colours
    ORDER BY Length(Colour) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment FROM Garments
    ORDER BY Length(Garment) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = f"""SELECT Clothes.ID, Clothes.Name,
    Brands.Brand_Name, Colours.Colour, Garments.Garment
    FROM Clothes
    LEFT JOIN Brands ON Clothes.Brand = Brands.ID  
    LEFT JOIN Garments ON Clothes.Garment = Garments.ID
    LEFT JOIN Colours ON Clothes.Colour = Colours.ID
    WHERE Clothes.Garment == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {nsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{nlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def addclothigitem(name, brand, colour, garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'''INSERT INTO Clothes (Name, Brand, Colour, Garment)
    VALUES ("{name}", "{brand}", "{colour}", "{garment}");'''
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


def removeclothingitem(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Clothes WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removebrand(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Brands WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removegarment():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Garments WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removecolour():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Colours WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


print("\nCharlotte's Digital Waldrobe <3")
while True:
    userinput = input("""
    Enter 'a' to view all clothes
    Enter 'b' to view all brands
    Enter 'c' to view all garment types
    Enter 'd' to view all colours
                      
    Enter 'e' to add a clothing item
    Enter 'f' to add a brand
    Enter 'g' to add a garment type
    Enter 'h' to add a color
                      
    Enter 'i' to remove a clothing item
    Enter 'j' to remove a brand
    Enter 'k' to remove a garment type
    Enter 'l' to remove a colour
                      
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
        fetchcolours()
    if userinput == 'e':
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
    if userinput == 'f':
        fetchallbrands()
        while True:
            brand = input("Enter New Brand Name: ").title()
            if brand == 'X':
                break
            else:
                addbrand(brand)
    if userinput == 'g':
        fetchallgarments()
        while True:
            garment = input("Enter New Garment Type: ").title()
            if garment == 'X':
                break
            else:
                addgarment(garment)
    if userinput == 'h':
        fetchcolours()
        while True:
            colour = input("Enter New Colour: ").title()
            if colour == 'X':
                break
            else:
                addcolour(colour)
    if userinput == 'i':
        fetchallclothes()
        while True:
            id = input("ID of clothing item to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() == False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() == True:
                if checkclothingidisvalid(id) == False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkclothingidisvalid(id) == True:
                    removeclothingitem(id)
                    break
    if userinput == 'j':
        fetchallbrands()
        while True:
            id = input("ID of brand to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() == False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() == True:
                if checkbrandidisvalid(id) == False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkbrandidisvalid(id) == True:
                    removebrand(id)
                    break
    if userinput == 'k':
        fetchallgarments()
        while True:
            id = input("ID of garment type to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() == False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() == True:
                if checkgarmentidisvalid(id) == False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkgarmentidisvalid(id) == True:
                    removegarment(id)
                    break
    if userinput == 'l':
        fetchcolours()
        while True:
            id = input("ID of colour to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() == False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() == True:
                if checkcolouridisvalid(id) == False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkcolouridisvalid(id) == True:
                    removecolour(id)
                    break
    if userinput == 'exit':
        break