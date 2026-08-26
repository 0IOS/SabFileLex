filename = input("Enter the filename: ")
char = input("Enter the character to count: ")

count = 0
with open(filename, 'r') as f:
    content = f.read()
    for c in content:
        if c == char:
            count = count + 1

print("The character '" + char + "' appears", count, "times in the file.")
