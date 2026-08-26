stack = []

numbers = input("Enter integers separated by space: ")
numbers = numbers.split()

for num in numbers:
    n = int(num)
    if n % 2 == 0:
        stack.append(n)

print("Even numbers pushed to stack:", stack)

print("\nPopping all elements:")
while len(stack) > 0:
    print(stack.pop(), end=" ")
print()
