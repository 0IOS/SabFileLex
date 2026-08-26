import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="company"
)
cursor = conn.cursor()

emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
emp_dept = input("Enter Department: ")
emp_desig = input("Enter Designation: ")
doj = input("Enter Date of Joining (YYYY-MM-DD): ")
salary = float(input("Enter Salary: "))

query = "INSERT INTO Employee (EmpID, EmpName, EmpDept, EmpDesig, DOJ, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
values = (emp_id, emp_name, emp_dept, emp_desig, doj, salary)
cursor.execute(query, values)
conn.commit()

print("\nRecord inserted successfully!")
print("\nDisplaying inserted record:")
cursor.execute("SELECT * FROM Employee WHERE EmpID = %s", (emp_id,))
record = cursor.fetchone()
print("EmpID:", record[0])
print("EmpName:", record[1])
print("EmpDept:", record[2])
print("EmpDesig:", record[3])
print("DOJ:", record[4])
print("Salary:", record[5])

cursor.close()
conn.close()
