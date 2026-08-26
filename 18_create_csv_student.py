import csv

n = int(input("How many students? "))

f = open("student.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["Name", "Roll No", "Gender", "Marks"])

for i in range(n):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    gender = input("Enter gender: ")
    marks = input("Enter marks: ")
    writer.writerow([name, roll, gender, marks])

f.close()
print("student.csv created successfully!")
