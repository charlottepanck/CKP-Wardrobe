import sqlite3

DB = 'ckpwardrobe.db'


def checkbottomidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Bottoms WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid


def checktopidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Tops WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid


def checkouterwearidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Outerwear WHERE ID == '{id}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) != 0:
        isvalid = True
    if len(results) == 0:
        isvalid = False
    return isvalid


def checkdressidisvalid(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"SELECT * FROM Dresses WHERE ID == '{id}';"
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
    # tops name column format
    sql1 = """SELECT Name FROM Tops
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = """SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nTops:\n| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # bottoms name column format
    sql1 = """SELECT Name FROM Bottoms
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        bnlg = len(x)
        bnsp = (bnlg-4) * " "
    # print table
    sql = """SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nBottoms:\n| ID | Name {bnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{bnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # outerwear name column format
    sql1 = """SELECT Name FROM Outerwear
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        onlg = len(x)
        onsp = (onlg-4) * " "
    # print table
    sql = """SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nOuterwear:\n| ID | Name {onsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{onlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # dresses name column format
    sql1 = """SELECT Name FROM Dresses
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        dnlg = len(x)
        dnsp = (dnlg-4) * " "
    # print table
    sql = """SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nDresses:\n| ID | Name {dnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{dnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchalldresses():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # Dresses name column format
    sql1 = """SELECT Name FROM Dresses
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = """SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchallouterwears():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # outerwear name column format
    sql1 = """SELECT Name FROM Outerwear
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        onlg = len(x)
        onsp = (onlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = """SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {onsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{onlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchallbottoms():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # bottoms name column format
    sql1 = """SELECT Name FROM Bottoms
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = """SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchalltops():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # tops name column format
    sql1 = """SELECT Name FROM Tops
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = """SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchclothesbycolour(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # tops name column format
    sql1 = """SELECT Name FROM Tops
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = f"""SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID
    WHERE Tops.Colour == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nTops:\n| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # bottoms name column format
    sql1 = """SELECT Name FROM Bottoms
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        bnlg = len(x)
        bnsp = (bnlg-4) * " "
    # print table
    sql = f"""SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID
    WHERE Bottoms.Colour == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nBottoms:\n| ID | Name {bnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{bnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # outerwear name column format
    sql1 = """SELECT Name FROM Outerwear
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        onlg = len(x)
        onsp = (onlg-4) * " "
    # print table
    sql = f"""SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID
    WHERE Outerwear.Colour == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nOuterwear:\n| ID | Name {onsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{onlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # dresses name column format
    sql1 = """SELECT Name FROM Dresses
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        dnlg = len(x)
        dnsp = (dnlg-4) * " "
    # print table
    sql = f"""SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID
    WHERE Dresses.Colour == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nDresses:\n| ID | Name {dnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{dnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchclothesbybrand(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # tops name column format
    sql1 = """SELECT Name FROM Tops
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = f"""SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID
    WHERE Tops.Brand == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"\nTops:\n| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # bottoms name column format
    sql1 = """SELECT Name FROM Bottoms
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        bnlg = len(x)
        bnsp = (bnlg-4) * " "
    # print table
    sql = f"""SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID
    WHERE Bottoms.Brand == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nBottoms:\n| ID | Name {bnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{bnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # outerwear name column format
    sql1 = """SELECT Name FROM Outerwear
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        onlg = len(x)
        onsp = (onlg-4) * " "
    # print table
    sql = f"""SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID
    WHERE Outerwear.Brand == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nOuterwear:\n| ID | Name {onsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{onlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # dresses name column format
    sql1 = """SELECT Name FROM Dresses
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        dnlg = len(x)
        dnsp = (dnlg-4) * " "
    # print table
    sql = f"""SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID
    WHERE Dresses.Brand == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nDresses:\n| ID | Name {dnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{dnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchclothesbygarment(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # tops name column format
    sql1 = """SELECT Name FROM Tops
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-4) * " "
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
    sql3 = """SELECT Colour_Type FROM Colours
    ORDER BY Length(Colour_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        clg = len(x)
        csp = (clg-6) * " "
    # garment column format
    sql3 = """SELECT Garment_Type FROM Garments
    ORDER BY Length(Garment_Type) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        glg = len(x)
        gsp = (glg-7) * " "
    # print table
    sql = f"""SELECT Tops.ID, Tops.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Tops
    LEFT JOIN Brands ON Tops.Brand = Brands.ID
    LEFT JOIN Garments ON Tops.Garment = Garments.ID
    LEFT JOIN Colours ON Tops.Colour = Colours.ID
    WHERE Tops.Garment == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nTops:\n| ID | Name {tnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # bottoms name column format
    sql1 = """SELECT Name FROM Bottoms
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        bnlg = len(x)
        bnsp = (bnlg-4) * " "
    # print table
    sql = f"""SELECT Bottoms.ID, Bottoms.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Bottoms
    LEFT JOIN Brands ON Bottoms.Brand = Brands.ID
    LEFT JOIN Garments ON Bottoms.Garment = Garments.ID
    LEFT JOIN Colours ON Bottoms.Colour = Colours.ID
    WHERE Bottoms.Garment == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nBottoms:\n| ID | Name {bnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{bnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # outerwear name column format
    sql1 = """SELECT Name FROM Outerwear
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        onlg = len(x)
        onsp = (onlg-4) * " "
    # print table
    sql = f"""SELECT Outerwear.ID, Outerwear.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Outerwear
    LEFT JOIN Brands ON Outerwear.Brand = Brands.ID
    LEFT JOIN Garments ON Outerwear.Garment = Garments.ID
    LEFT JOIN Colours ON Outerwear.Colour = Colours.ID
    WHERE Outerwear.Garment == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nOuterwear:\n| ID | Name {onsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{onlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")

    # dresses name column format
    sql1 = """SELECT Name FROM Dresses
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        dnlg = len(x)
        dnsp = (dnlg-4) * " "
    # print table
    sql = f"""SELECT Dresses.ID, Dresses.Name,
    Brands.Brand_Name, Colours.Colour_Type, Garments.Garment_Type
    FROM Dresses
    LEFT JOIN Brands ON Dresses.Brand = Brands.ID
    LEFT JOIN Garments ON Dresses.Garment = Garments.ID
    LEFT JOIN Colours ON Dresses.Colour = Colours.ID
    WHERE Dresses.Garment == '{id}';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nDresses:\n| ID | Name {dnsp}| Brand {bsp}| Colour {csp}| Garment {gsp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{dnlg}} | {i[2]:{blg}} | {i[3]:{clg}} | {i[4]:{glg}} |")
    db.close


def fetchalloutfits():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    # tops name column format
    sql1 = """SELECT Name FROM Tops
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tnlg = len(x)
        tnsp = (tnlg-3) * " "
    # bottoms name column format
    sql2 = """SELECT Name FROM Bottoms
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        bnlg = len(x)
        bnsp = (bnlg-6) * " "
    # outerwear name column format
    sql3 = """SELECT Name FROM Outerwear
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        onlg = len(x)
        onsp = (onlg-9) * " "
    # dresses name column format
    sql4 = """SELECT Name FROM Dresses
    ORDER BY Length(Name) desc LIMIT 1;"""
    cursor.execute(sql4)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        dnlg = len(x)
        dnsp = (dnlg-5) * " "
    # style column format
    sql5 = """SELECT Style_Name FROM Styles
    ORDER BY Length(Style_Name) desc LIMIT 1;"""
    cursor.execute(sql5)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-5) * " "
    sql = """SELECT Outfits.ID, Tops.Name, Bottoms.Name, Outerwear.Name, Dresses.Name, Styles.Style_Name
    FROM Outfits
    LEFT JOIN Tops ON Outfits.Top == Tops.ID
    LEFT JOIN Bottoms ON Outfits.Bottoms == Bottoms.ID
    LEFT JOIN Outerwear ON Outfits.Outerwear == Outerwear.ID
    LEFT JOIN Dresses ON Outfits.Dress == Dresses.ID
    LEFT JOIN Styles ON Outfits.Style == Styles.ID;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"| ID | Top {tnsp}| Bottom {bnsp}| Outerwear {onsp}| Dress {dnsp}| Style {ssp}|")
    for i in results:
        print(f"| {i[0]:2} | {i[1]:{tnlg}} | {i[2]:{bnlg}} | {i[3]:{onlg}} | {i[4]:{dnlg}} | {i[5]:{slg}} |")
    db.close


def addtop(name, brand, colour, garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'''INSERT INTO Tops (Name, Brand, Colour, Garment)
    VALUES ("{name}", "{brand}", "{colour}", "{garment}");'''
    cursor.execute(sql)
    db.commit()


def addbottom(name, brand, colour, garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'''INSERT INTO Bottoms (Name, Brand, Colour, Garment)
    VALUES ("{name}", "{brand}", "{colour}", "{garment}");'''
    cursor.execute(sql)
    db.commit()


def addouterwear(name, brand, colour, garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'''INSERT INTO Outerwear (Name, Brand, Colour, Garment)
    VALUES ("{name}", "{brand}", "{colour}", "{garment}");'''
    cursor.execute(sql)
    db.commit()


def adddress(name, brand, colour, garment):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'''INSERT INTO Dresses (Name, Brand, Colour, Garment)
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
    sql = f'INSERT INTO Garments (Garment_Type) VALUES ("{garment}");'
    cursor.execute(sql)
    db.commit()


def addcolour(colour):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'INSERT INTO Colours (Colour_Type) VALUES ("{colour}");'
    cursor.execute(sql)
    db.commit()


def removetop(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Tops WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removebottom(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Bottoms WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removeouterwear(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Outerwear WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removedress(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Dresses WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removebrand(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Brands WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removegarment(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Garments WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


def removecolour(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Colours WHERE ID = {id};"
    cursor.execute(sql)
    db.commit()


print("\nCharlotte's Digital Wardrobe <3")
while True:
    userinput = input("""
    Enter 'a' to view all clothes
    Enter 'b' to view all brands
    Enter 'c' to view all garment types
    Enter 'd' to view all colours

    Enter 'e' to add a top
    Enter 'f' to add a bottom
    Enter 'g' to add outerwear item
    Enter 'h' to add a dress
    Enter 'i' to add a brand
    Enter 'j' to add a garment type
    Enter 'k' to add a color

    Enter 'l' to remove a top
    Enter 'm' to remove a bottom
    Enter 'n' to remove an outerwear item
    Enter 'o' to remove a dress
    Enter 'p' to remove a brand
    Enter 'q' to remove a garment type
    Enter 'r' to remove a colour

    Enter 's' to view outfits
    Enter 't' to add an outfit
    Enter 'u' to remove an outfit

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
    Enter 'd' to show tops only
    Enter 'e' to show bottoms only
    Enter 'f' to show outerwear only
    Enter 'g' to show dresses only
    >>> """).lower()
            if userinput1 == 'a':
                fetchcolours()
                while True:
                    id = input("\nEnter Colour ID: ")
                    if id == 'x' or id == 'X':
                        break
                    if id.isnumeric() is True:
                        if checkcolouridisvalid(id) is True:
                            fetchclothesbycolour(id)
                            break
                        if checkcolouridisvalid(id) is False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() is False:
                        print("\nInvalid Input!\nID must be an Integer.\nTry Again...")
            if userinput1 == 'b':
                fetchallbrands()
                while True:
                    id = input("\nEnter Brand ID: ")
                    if id == 'x' or id == 'X':
                        break
                    if id.isnumeric() is True:
                        if checkbrandidisvalid(id) is True:
                            fetchclothesbybrand(id)
                            break
                        if checkbrandidisvalid(id) is False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() is False:
                        print("\nInvalid Input!\nID must be an Integer.\nTry Again...")
            if userinput1 == 'c':
                fetchallgarments()
                while True:
                    id = input("\nEnter Garment ID: ")
                    if id == 'x' or id == 'X':
                        break
                    if id.isnumeric() is True:
                        if checkgarmentidisvalid(id) is True:
                            fetchclothesbygarment(id)
                            break
                        if checkgarmentidisvalid(id) is False:
                            print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...")
                    if id.isnumeric() is False:
                        print("\nInvalid Input!\nID must be an Integer.\nTry Again...")
            if userinput1 == 'd':
                fetchalltops()
            if userinput1 == 'e':
                fetchallbottoms()
            if userinput1 == 'f':
                fetchallouterwears()
            if userinput1 == 'g':
                fetchalldresses()
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
            if flag is True:
                break
            name = input("Name: ").title()
            if name == 'x' or name == 'X':
                break
            fetchallbrands()
            while True:
                if flag is True:
                    break
                brand = input("Brand ID: ").lower()
                if brand == 'x':
                    flag = True
                elif brand.isnumeric() is False:
                    print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                elif brand.isnumeric() is True:
                    if checkbrandidisvalid(brand) is False:
                        print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                    if checkbrandidisvalid(brand) is True:
                        fetchcolours()
                        while True:
                            if flag is True:
                                break
                            colour = input("Colour ID: ").lower()
                            if colour == 'x':
                                flag = True
                            elif colour.isnumeric() is False:
                                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                            elif colour.isnumeric() is True:
                                if checkcolouridisvalid(colour) is False:
                                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                if checkcolouridisvalid(colour) is True:
                                    fetchallgarments()
                                    while True:
                                        if flag is True:
                                            break
                                        garment = input("Garment ID: ").lower()
                                        if garment == 'x':
                                            flag = True
                                        elif garment.isnumeric() is False:
                                            print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                                        elif garment.isnumeric() is True:
                                            if checkgarmentidisvalid(garment) is False:
                                                print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                            if checkgarmentidisvalid(garment) is True:
                                                addtop(name, brand, colour, garment)
                                                flag = True
                                                break
    if userinput == 'f':
        flag = False
        while True:
            if flag is True:
                break
            name = input("Name: ").title()
            if name == 'x' or name == 'X':
                break
            fetchallbrands()
            while True:
                if flag is True:
                    break
                brand = input("Brand ID: ").lower()
                if brand == 'x':
                    flag = True
                elif brand.isnumeric() is False:
                    print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                elif brand.isnumeric() is True:
                    if checkbrandidisvalid(brand) is False:
                        print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                    if checkbrandidisvalid(brand) is True:
                        fetchcolours()
                        while True:
                            if flag is True:
                                break
                            colour = input("Colour ID: ").lower()
                            if colour == 'x':
                                flag = True
                            elif colour.isnumeric() is False:
                                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                            elif colour.isnumeric() is True:
                                if checkcolouridisvalid(colour) is False:
                                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                if checkcolouridisvalid(colour) is True:
                                    fetchallgarments()
                                    while True:
                                        if flag is True:
                                            break
                                        garment = input("Garment ID: ").lower()
                                        if garment == 'x':
                                            flag = True
                                        elif garment.isnumeric() is False:
                                            print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                                        elif garment.isnumeric() is True:
                                            if checkgarmentidisvalid(garment) is False:
                                                print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                            if checkgarmentidisvalid(garment) is True:
                                                addbottom(name, brand, colour, garment)
                                                flag = True
                                                break
    if userinput == 'g':
        flag = False
        while True:
            if flag is True:
                break
            name = input("Name: ").title()
            if name == 'x' or name == 'X':
                break
            fetchallbrands()
            while True:
                if flag is True:
                    break
                brand = input("Brand ID: ").lower()
                if brand == 'x':
                    flag = True
                elif brand.isnumeric() is False:
                    print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                elif brand.isnumeric() is True:
                    if checkbrandidisvalid(brand) is False:
                        print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                    if checkbrandidisvalid(brand) is True:
                        fetchcolours()
                        while True:
                            if flag is True:
                                break
                            colour = input("Colour ID: ").lower()
                            if colour == 'x':
                                flag = True
                            elif colour.isnumeric() is False:
                                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                            elif colour.isnumeric() is True:
                                if checkcolouridisvalid(colour) is False:
                                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                if checkcolouridisvalid(colour) is True:
                                    fetchallgarments()
                                    while True:
                                        if flag is True:
                                            break
                                        garment = input("Garment ID: ").lower()
                                        if garment == 'x':
                                            flag = True
                                        elif garment.isnumeric() is False:
                                            print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                                        elif garment.isnumeric() is True:
                                            if checkgarmentidisvalid(garment) is False:
                                                print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                            if checkgarmentidisvalid(garment) is True:
                                                addouterwear(name, brand, colour, garment)
                                                flag = True
                                                break
    if userinput == 'h':
        flag = False
        while True:
            if flag is True:
                break
            name = input("Name: ").title()
            if name == 'x' or name == 'X':
                break
            fetchallbrands()
            while True:
                if flag is True:
                    break
                brand = input("Brand ID: ").lower()
                if brand == 'x':
                    flag = True
                elif brand.isnumeric() is False:
                    print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                elif brand.isnumeric() is True:
                    if checkbrandidisvalid(brand) is False:
                        print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                    if checkbrandidisvalid(brand) is True:
                        fetchcolours()
                        while True:
                            if flag is True:
                                break
                            colour = input("Colour ID: ").lower()
                            if colour == 'x':
                                flag = True
                            elif colour.isnumeric() is False:
                                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                            elif colour.isnumeric() is True:
                                if checkcolouridisvalid(colour) is False:
                                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                if checkcolouridisvalid(colour) is True:
                                    fetchallgarments()
                                    while True:
                                        if flag is True:
                                            break
                                        garment = input("Garment ID: ").lower()
                                        if garment == 'x':
                                            flag = True
                                        elif garment.isnumeric() is False:
                                            print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
                                        elif garment.isnumeric() is True:
                                            if checkgarmentidisvalid(garment) is False:
                                                print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                                            if checkgarmentidisvalid(garment) is True:
                                                adddress(name, brand, colour, garment)
                                                flag = True
                                                break
    if userinput == 'i':
        fetchallbrands()
        while True:
            brand = input("Enter New Brand Name: ").title()
            if brand == 'X':
                break
            else:
                addbrand(brand)
                break
    if userinput == 'j':
        fetchallgarments()
        while True:
            garment = input("Enter New Garment Type: ").title()
            if garment == 'X':
                break
            else:
                addgarment(garment)
                break
    if userinput == 'k':
        fetchcolours()
        while True:
            colour = input("Enter New Colour: ").title()
            if colour == 'X':
                break
            else:
                addcolour(colour)
                break
    if userinput == 'l':
        fetchalltops()
        while True:
            id = input("ID of top to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checktopidisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checktopidisvalid(id) is True:
                    removetop(id)
                    break
    if userinput == 'm':
        fetchallbottoms()
        while True:
            id = input("ID of bottom to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checkbottomidisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkbottomidisvalid(id) is True:
                    removebottom(id)
                    break
    if userinput == 'n':
        fetchallouterwears()
        while True:
            id = input("ID of outerwear item to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checkouterwearidisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkouterwearidisvalid(id) is True:
                    removeouterwear(id)
                    break
    if userinput == 'o':
        fetchalldresses()
        while True:
            id = input("ID of dress to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checkdressidisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkdressidisvalid(id) is True:
                    removedress(id)
                    break
    if userinput == 'p':
        fetchallbrands()
        while True:
            id = input("ID of brand to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checkbrandidisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkbrandidisvalid(id) is True:
                    removebrand(id)
                    break
    if userinput == 'q':
        fetchallgarments()
        while True:
            id = input("ID of garment type to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checkgarmentidisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkgarmentidisvalid(id) is True:
                    removegarment(id)
                    break
    if userinput == 'r':
        fetchcolours()
        while True:
            id = input("ID of colour to be deleted: ")
            if id == 'x' or id == 'X':
                break
            if id.isnumeric() is False:
                print("\nInvalid Input!\nID must be an Integer.\nTry Again...\n")
            if id.isnumeric() is True:
                if checkcolouridisvalid(id) is False:
                    print("\nInvalid Input!\nID Doesn't Exsist.\nTry Again...\n")
                if checkcolouridisvalid(id) is True:
                    removecolour(id)
                    break
    if userinput == 's':
        print("\ni havent finished this section yet :p")
        fetchalloutfits()
    if userinput == 't':
        print("\ni havent written this section yet :p")
    if userinput == 'u':
        print("\ni havent written this section yet :p")
    if userinput == 'exit':
        break
