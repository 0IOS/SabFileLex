import csv

f = open("student.csv", "r")
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()
