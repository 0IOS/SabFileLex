stack = []

string = input("Enter a string: ")

for char in string:
    if char.lower() in 'aeiou':
        stack.append(char)

print("Vowels pushed to stack:", stack)

print("\nPopping all vowels:")
while len(stack) > 0:
    print(stack.pop(), end=" ")
print()
