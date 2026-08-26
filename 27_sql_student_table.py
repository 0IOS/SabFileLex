import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE student (
    RollNo INTEGER PRIMARY KEY,
    Name TEXT,
    Class TEXT,
    Section TEXT,
    Marks INTEGER
)''')

students = [
    (1, 'Rahul', '12', 'A', 85),
    (2, 'Priya', '12', 'B', 92),
    (3, 'Amit', '11', 'A', 78),
    (4, 'Sneha', '12', 'A', 88),
    (5, 'Rohan', '11', 'B', 65),
    (6, 'Neha', '12', 'B', 91),
    (7, 'Vikram', '11', 'A', 72),
    (8, 'Pooja', '12', 'A', 95),
    (9, 'Arjun', '11', 'B', 80),
    (10, 'Divya', '12', 'B', 70)
]
c.executemany('INSERT INTO student VALUES (?,?,?,?,?)', students)
conn.commit()

print("=== Original Student Table ===")
c.execute("SELECT * FROM student")
for row in c.fetchall():
    print(row)

print("\n=== ALTER TABLE - Add Column ===")
c.execute("ALTER TABLE student ADD COLUMN Grade TEXT")
c.execute("UPDATE student SET Grade='A' WHERE Marks>=90")
c.execute("UPDATE student SET Grade='B' WHERE Marks>=80 AND Marks<90")
c.execute("UPDATE student SET Grade='C' WHERE Marks>=70 AND Marks<80")
c.execute("UPDATE student SET Grade='D' WHERE Marks<70")
conn.commit()
c.execute("SELECT * FROM student")
for row in c.fetchall():
    print(row)

print("\n=== ALTER TABLE - Drop Column ===")
c.execute("ALTER TABLE student DROP COLUMN Grade")
conn.commit()
c.execute("SELECT * FROM student")
for row in c.fetchall():
    print(row)

print("\n=== UPDATE Table ===")
c.execute("UPDATE student SET Marks=90 WHERE RollNo=3")
conn.commit()
c.execute("SELECT * FROM student WHERE RollNo=3")
print("After updating RollNo=3:", c.fetchone())

print("\n=== ORDER BY Ascending ===")
c.execute("SELECT * FROM student ORDER BY Marks ASC")
for row in c.fetchall():
    print(row)

print("\n=== ORDER BY Descending ===")
c.execute("SELECT * FROM student ORDER BY Marks DESC")
for row in c.fetchall():
    print(row)

print("\n=== DELETE ===")
c.execute("DELETE FROM student WHERE RollNo=10")
conn.commit()
c.execute("SELECT * FROM student")
for row in c.fetchall():
    print(row)

print("\n=== GROUP BY with MIN, MAX, SUM, COUNT, AVG ===")
c.execute('''SELECT Class, MIN(Marks), MAX(Marks), SUM(Marks), COUNT(*), AVG(Marks)
             FROM student GROUP BY Class''')
print("Class | Min | Max | Sum | Count | Avg")
for row in c.fetchall():
    print(row)

conn.close()
