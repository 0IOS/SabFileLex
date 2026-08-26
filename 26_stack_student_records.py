stack = []

def push_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    gpa = float(input("Enter GPA: "))
    if gpa > 60:
        stack.append({"student_id": student_id, "name": name, "gpa": gpa})
        print("Student pushed to stack!")
    else:
        print("GPA must be above 60 to push.")

def pop_student():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        student = stack.pop()
        print("Popped Student:")
        print("ID:", student["student_id"])
        print("Name:", student["name"])
        print("GPA:", student["gpa"])

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("--- Student Records in Stack ---")
        for i in range(len(stack) - 1, -1, -1):
            print("ID:", stack[i]["student_id"])
            print("Name:", stack[i]["name"])
            print("GPA:", stack[i]["gpa"])
            print("---")

while True:
    print("\n--- Student Stack Operations ---")
    print("1. Push Student")
    print("2. Pop Student")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        push_student()
    elif choice == '2':
        pop_student()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
