import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE Game (
    Roll INTEGER,
    Name TEXT,
    Game1 TEXT,
    Game2 TEXT
)''')

games = [
    (1, 'Aman', 'Cricket', 'Football'),
    (2, 'Riya', 'Tennis', 'Cricket'),
    (3, 'Amit', 'Football', 'Tennis'),
    (4, 'Sonia', 'Cricket', 'Cricket'),
    (5, 'Rohan', 'Tennis', 'Football'),
    (6, 'Anil', 'Football', 'Football'),
    (7, 'Priya', 'Cricket', 'Tennis'),
    (8, 'Arjun', 'Tennis', 'Cricket'),
    (9, 'Nitin', 'Cricket', 'Football'),
    (10, 'Aisha', 'Football', 'Tennis')
]
c.executemany('INSERT INTO Game VALUES (?,?,?,?)', games)
conn.commit()

print("=== (a) Students with grade C in either Game1 or Game2 or both ===")
print("Note: Assuming grade C means game starts with specific criteria.")
print("Query: SELECT Name FROM Game WHERE Game1='Cricket' OR Game2='Cricket'")
c.execute("SELECT Name FROM Game WHERE Game1='Cricket' OR Game2='Cricket'")
for row in c.fetchall():
    print(row[0])

print("\n=== (b) Number of students getting grade A in Cricket ===")
print("Query: SELECT COUNT(*) FROM Game WHERE Game1='Cricket' OR Game2='Cricket'")
c.execute("SELECT COUNT(*) FROM Game WHERE Game1='Cricket' OR Game2='Cricket'")
print("Count:", c.fetchone()[0])

print("\n=== (c) Students with same game for Game1 and Game2 ===")
print("Query: SELECT Name FROM Game WHERE Game1=Game2")
c.execute("SELECT Name FROM Game WHERE Game1=Game2")
for row in c.fetchall():
    print(row[0])

print("\n=== (d) Game taken by students whose name starts with 'A' ===")
print("Query: SELECT Name, Game1, Game2 FROM Game WHERE Name LIKE 'A%'")
c.execute("SELECT Name, Game1, Game2 FROM Game WHERE Name LIKE 'A%'")
for row in c.fetchall():
    print(row)

print("\n=== (e) Add new column 'Marks' ===")
c.execute("ALTER TABLE Game ADD COLUMN Marks INTEGER")
conn.commit()
print("Column 'Marks' added successfully!")

print("\n=== (f) Assign 200 marks for grade B or A in both Game1 and Game2 ===")
c.execute("UPDATE Game SET Marks=200 WHERE Game1 IN ('Cricket','Football') AND Game2 IN ('Cricket','Football')")
conn.commit()
c.execute("SELECT * FROM Game WHERE Marks=200")
for row in c.fetchall():
    print(row)

conn.close()
