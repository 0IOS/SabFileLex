stack = []

def push(item):
    stack.append(item)
    print(item, "pushed to stack")

def pop():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        item = stack.pop()
        print(item, "popped from stack")

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack:", stack)

while True:
    print("\n--- Stack Operations ---")
    print("1. PUSH")
    print("2. POP")
    print("3. Display")
    print("4. EXIT")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter element to push: ")
        push(item)
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
