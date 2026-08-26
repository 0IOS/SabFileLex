import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE Client (
    Client_ID INTEGER PRIMARY KEY,
    Name TEXT,
    City TEXT,
    Phone TEXT
)''')

c.execute('''CREATE TABLE Product (
    Product_ID INTEGER PRIMARY KEY,
    Product_Name TEXT,
    Price INTEGER,
    Manufacturer TEXT
)''')

clients = [
    (1, 'Rakesh', 'Delhi', '9876543210'),
    (2, 'Suresh', 'Mumbai', '9876543211'),
    (3, 'Mahesh', 'Delhi', '9876543212'),
    (4, 'Rajesh', 'Chennai', '9876543213'),
    (5, 'Dinesh', 'Delhi', '9876543214')
]
c.executemany('INSERT INTO Client VALUES (?,?,?,?)', clients)

products = [
    (1, 'Surf Wash', 80, 'HUL'),
    (2, 'Ariel Wash', 120, 'P&G'),
    (3, 'Nirma Wash', 45, 'Nirma'),
    (4, 'Tide Wash', 95, 'P&G'),
    (5, 'Wheel Wash', 35, 'HUL')
]
c.executemany('INSERT INTO Product VALUES (?,?,?,?)', products)
conn.commit()

print("=== Clients in Delhi ===")
c.execute("SELECT * FROM Client WHERE City='Delhi'")
for row in c.fetchall():
    print(row)

print("\n=== Products with Price between 50 and 100 ===")
c.execute("SELECT * FROM Product WHERE Price BETWEEN 50 AND 100")
for row in c.fetchall():
    print(row)

print("\n=== Products whose name ends with 'Wash' ===")
c.execute("SELECT * FROM Product WHERE Product_Name LIKE '%Wash'")
for row in c.fetchall():
    print(row)

print("\n=== Select Distinct City from Client ===")
c.execute("SELECT DISTINCT City FROM Client")
for row in c.fetchall():
    print(row)

print("\n=== Manufacturer, Max, Min, Count from Product ===")
c.execute("SELECT Manufacturer, MAX(Price), MIN(Price), COUNT(*) FROM Product GROUP BY Manufacturer")
for row in c.fetchall():
    print(row)

print("\n=== Product Name, Price * 4 ===")
c.execute("SELECT Product_Name, Price * 4 FROM Product")
for row in c.fetchall():
    print(row)

conn.close()
