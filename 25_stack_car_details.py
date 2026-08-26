stack = []

def push(car):
    stack.append(car)
    print("Car added to stack!")

def pop():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        car = stack.pop()
        print("Car removed:")
        print("Car No:", car["car_no"])
        print("Car Make:", car["car_make"])
        print("Price:", car["price"])

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("--- Car Details in Stack ---")
        for i in range(len(stack) - 1, -1, -1):
            print("Car No:", stack[i]["car_no"])
            print("Car Make:", stack[i]["car_make"])
            print("Price:", stack[i]["price"])
            print("---")

while True:
    print("\n--- Car Stack Operations ---")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")
    choice = input("Enter your choice: ")

    if choice == '1':
        car_no = input("Enter car number: ")
        car_make = input("Enter car make: ")
        price = float(input("Enter price: "))
        push({"car_no": car_no, "car_make": car_make, "price": price})
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
