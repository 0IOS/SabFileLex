import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE Company (
    Comp_ID INTEGER PRIMARY KEY,
    CompName TEXT,
    ContactPerson TEXT,
    CompHO TEXT
)''')

c.execute('''CREATE TABLE Model (
    Model_ID INTEGER PRIMARY KEY,
    Comp_ID INTEGER,
    Model_Name TEXT,
    DateOfManufacture TEXT,
    Cost INTEGER,
    FOREIGN KEY (Comp_ID) REFERENCES Company(Comp_ID)
)''')

companies = [
    (1, 'Tata', 'Ratan Tata', 'Mumbai'),
    (2, 'Mahindra', 'Anand Mahindra', 'Pune'),
    (3, 'Maruti', 'R.C. Bhargava', 'Delhi'),
    (4, 'Hyundai', 'Y.K. Choi', 'Chennai')
]
c.executemany('INSERT INTO Company VALUES (?,?,?,?)', companies)

models = [
    (101, 1, 'Nexon', '2011-03-15', 1500),
    (102, 1, 'Harrier', '2011-07-20', 2500),
    (103, 2, 'Thar', '2011-01-10', 1800),
    (104, 2, 'XUV700', '2011-11-05', 1900),
    (105, 3, 'Swift', '2011-05-25', 1200),
    (106, 3, 'Baleno', '2011-09-30', 800),
    (107, 4, 'Creta', '2011-06-18', 1600),
    (108, 4, 'Venue', '2011-12-01', 500)
]
c.executemany('INSERT INTO Model VALUES (?,?,?,?,?)', models)
conn.commit()

print("=== (i) Models in ascending order of DateOfManufacture ===")
c.execute("SELECT * FROM Model ORDER BY DateOfManufacture ASC")
for row in c.fetchall():
    print(row)

print("\n=== (ii) Models manufactured in 2011 with Cost below 2000 ===")
c.execute("SELECT * FROM Model WHERE DateOfManufacture LIKE '2011%' AND Cost < 2000")
for row in c.fetchall():
    print(row)

print("\n=== (iii) Model_ID, Comp_ID, Cost, CompName, ContactPerson ===")
c.execute('''SELECT m.Model_ID, m.Comp_ID, m.Cost, c.CompName, c.ContactPerson
             FROM Model m, Company c WHERE m.Comp_ID = c.Comp_ID''')
for row in c.fetchall():
    print(row)

print("\n=== (iv) Decrease cost of all models by 15% ===")
c.execute("UPDATE Model SET Cost = Cost - (Cost * 0.15)")
conn.commit()
c.execute("SELECT * FROM Model")
for row in c.fetchall():
    print(row)

print("\n=== (v) Count distinct CompHO from Company ===")
c.execute("SELECT COUNT(DISTINCT CompHO) FROM Company")
print("Count:", c.fetchone()[0])

print("\n=== (vi) CompName ending with 'a' with Mr. prefix ===")
c.execute("SELECT CompName, 'Mr.' || ContactPerson FROM Company WHERE CompName LIKE '%a'")
for row in c.fetchall():
    print(row)

conn.close()
