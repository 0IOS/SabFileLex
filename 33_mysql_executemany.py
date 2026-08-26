import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="company"
)
cursor = conn.cursor()

records = []
for i in range(5):
    print("\nEnter details for employee", i + 1, ":")
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_dept = input("Enter Department: ")
    emp_desig = input("Enter Designation: ")
    doj = input("Enter Date of Joining (YYYY-MM-DD): ")
    salary = float(input("Enter Salary: "))
    records.append((emp_id, emp_name, emp_dept, emp_desig, doj, salary))

query = "INSERT INTO Employee (EmpID, EmpName, EmpDept, EmpDesig, DOJ, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(query, records)
conn.commit()

print("\n", cursor.rowcount, "records inserted successfully!")

print("\nDisplaying all records:")
cursor.execute("SELECT * FROM Employee")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
