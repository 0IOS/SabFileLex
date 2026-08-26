import pickle

def create_file():
    n = int(input("How many students? "))
    f = open("student_marks.dat", "wb")
    for i in range(n):
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        pickle.dump({"roll": roll, "name": name, "marks": marks}, f)
    f.close()
    print("File created successfully!")

def update_marks():
    search_roll = int(input("Enter roll number to update: "))
    f = open("student_marks.dat", "rb")
    students = []
    try:
        while True:
            student = pickle.load(f)
            students.append(student)
    except EOFError:
        f.close()

    found = False
    for i in range(len(students)):
        if students[i]["roll"] == search_roll:
            print("Current record:")
            print("Roll:", students[i]["roll"], "Name:", students[i]["name"], "Marks:", students[i]["marks"])
            new_marks = float(input("Enter new marks: "))
            students[i]["marks"] = new_marks
            found = True
            break

    if found:
        f = open("student_marks.dat", "wb")
        for s in students:
            pickle.dump(s, f)
        f.close()
        print("Marks updated successfully!")
    else:
        print("Student with roll number", search_roll, "not found.")

print("1. Create Binary File")
print("2. Update Marks")
choice = input("Enter your choice: ")

if choice == '1':
    create_file()
elif choice == '2':
    update_marks()
else:
    print("Invalid choice!")
