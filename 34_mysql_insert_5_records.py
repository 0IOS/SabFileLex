import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="company"
)
cursor = conn.cursor()

for i in range(5):
    print("\nEnter details for employee", i + 1, ":")
    emp_id = input("Enter Emp_ID: ")
    emp_name = input("Enter Emp_Name: ")
    doj = input("Enter DOJ (YYYY-MM-DD): ")
    gender = input("Enter Gender: ")
    salary = float(input("Enter Salary: "))

    query = "INSERT INTO Employee (Emp_ID, Emp_Name, DOJ, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (emp_id, emp_name, doj, gender, salary))
    conn.commit()
    print("Record inserted!")

print("\n--- All Employee Records ---")
cursor.execute("SELECT * FROM Employee")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
