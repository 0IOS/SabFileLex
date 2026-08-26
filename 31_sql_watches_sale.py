import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE Watches (
    watchid INTEGER PRIMARY KEY,
    watch_name TEXT,
    type TEXT,
    qty_store INTEGER,
    price INTEGER
)''')

c.execute('''CREATE TABLE Sale (
    saleid INTEGER PRIMARY KEY,
    watchid INTEGER,
    quarter TEXT,
    qty_sold INTEGER,
    FOREIGN KEY (watchid) REFERENCES Watches(watchid)
)''')

watches = [
    (1, 'Titan', 'Analog', 100, 2500),
    (2, 'Casio', 'Digital', 200, 1500),
    (3, 'Fossil', 'Analog', 150, 5000),
    (4, 'Sonata', 'Digital', 300, 800),
    (5, 'G-Shock', 'Digital', 120, 4000)
]
c.executemany('INSERT INTO Watches VALUES (?,?,?,?,?)', watches)

sales = [
    (1, 1, 'Q1', 10),
    (2, 2, 'Q2', 25),
    (3, 3, 'Q1', 15),
    (4, 1, 'Q2', 8),
    (5, 4, 'Q3', 40),
    (6, 5, 'Q1', 5),
    (7, 2, 'Q3', 30),
    (8, 3, 'Q2', 12)
]
c.executemany('INSERT INTO Sale VALUES (?,?,?,?)', sales)
conn.commit()

print("=== (i) Quarter-wise total qty_sold ===")
print("Query: select quarter, sum(qty_sold) from sale group by quarter;")
c.execute("SELECT quarter, SUM(qty_sold) FROM Sale GROUP BY quarter")
print(f"{'Quarter':<10} {'SUM(qty_sold)':<15}")
print("-" * 25)
for row in c.fetchall():
    print(f"{row[0]:<10} {row[1]:<15}")

print("\n=== (ii) Watches with watchid != sale watchid (cross non-match) ===")
print("Query: select watch_name, price, type from watches w, sale s where w.watchid != s.watchid;")
c.execute("SELECT DISTINCT w.watch_name, w.price, w.type FROM Watches w, Sale s WHERE w.watchid != s.watchid")
print(f"{'watch_name':<15} {'price':<10} {'type':<10}")
print("-" * 35)
for row in c.fetchall():
    print(f"{row[0]:<15} {row[1]:<10} {row[2]:<10}")

print("\n=== (iii) Watch details with stock calculation ===")
print("Query: select watch_name, qty_store, sum(qty_sold), qty_store-sum(qty_sold) Stock")
print("       from Watches w, sale s where w.watchid=s.watchid group by s.watchid;")
c.execute('''SELECT w.watch_name, w.qty_store, SUM(s.qty_sold),
             w.qty_store - SUM(s.qty_sold) as Stock
             FROM Watches w, Sale s WHERE w.watchid = s.watchid GROUP BY s.watchid''')
print(f"{'watch_name':<15} {'qty_store':<10} {'SUM(qty_sold)':<15} {'Stock':<10}")
print("-" * 50)
for row in c.fetchall():
    print(f"{row[0]:<15} {row[1]:<10} {row[2]:<15} {row[3]:<10}")

conn.close()
