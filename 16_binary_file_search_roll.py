import pickle

def create_file():
    n = int(input("How many students? "))
    f = open("students.dat", "wb")
    for i in range(n):
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        pickle.dump({"name": name, "roll": roll}, f)
    f.close()
    print("File created successfully!")

def search_student():
    search_roll = int(input("Enter roll number to search: "))
    f = open("students.dat", "rb")
    found = False
    try:
        while True:
            student = pickle.load(f)
            if student["roll"] == search_roll:
                print("Student Found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                found = True
                break
    except EOFError:
        f.close()
    if not found:
        print("Student with roll number", search_roll, "not found.")

print("1. Create Binary File")
print("2. Search Student")
choice = input("Enter your choice: ")

if choice == '1':
    create_file()
elif choice == '2':
    search_student()
else:
    print("Invalid choice!")
