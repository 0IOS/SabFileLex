import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="company"
)
cursor = conn.cursor()

print("Current record with Emp_ID = E1001:")
cursor.execute("SELECT * FROM Employee WHERE Emp_ID = 'E1001'")
record = cursor.fetchone()
if record:
    print("Emp_ID:", record[0])
    print("Emp_Name:", record[1])
    print("DOJ:", record[2])
    print("Gender:", record[3])
    print("Salary:", record[4])
else:
    print("Record not found!")

new_name = input("\nEnter new name for employee E1001: ")

query = "UPDATE Employee SET Emp_Name = %s WHERE Emp_ID = 'E1001'"
cursor.execute(query, (new_name,))
conn.commit()

print("\nRecord updated successfully!")
print("\nUpdated record:")
cursor.execute("SELECT * FROM Employee WHERE Emp_ID = 'E1001'")
record = cursor.fetchone()
print("Emp_ID:", record[0])
print("Emp_Name:", record[1])
print("DOJ:", record[2])
print("Gender:", record[3])
print("Salary:", record[4])

cursor.close()
conn.close()
