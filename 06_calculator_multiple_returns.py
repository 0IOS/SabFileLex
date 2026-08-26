def calculator(a, b):
    return a + b, a - b, a * b, a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition, subtraction, multiplication, division = calculator(num1, num2)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
