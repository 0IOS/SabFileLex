# int() - converts a value to integer
print("int():", int(3.7))        # Output: 3
print("int():", int("10"))       # Output: 10

# str() - converts a value to string
print("str():", str(100))        # Output: '100'

# float() - converts a value to float
print("float():", float(5))      # Output: 5.0

# input() - takes input from user (demonstrated conceptually)
# x = input("Enter something: ")

# eval() - evaluates a string as expression
print("eval():", eval("3 + 5"))  # Output: 8

# max() - returns maximum value
print("max():", max(10, 20, 30)) # Output: 30

# abs() - returns absolute value
print("abs():", abs(-15))        # Output: 15

# type() - returns type of object
print("type():", type(10))       # Output: <class 'int'>

# len() - returns length
print("len():", len("Hello"))    # Output: 5

# round() - rounds a number
print("round():", round(3.567, 2))  # Output: 3.57

# range() - generates a range of numbers
print("range():", list(range(1, 6)))  # Output: [1, 2, 3, 4, 5]

# bytes() - returns immutable bytes object
print("bytes():", bytes(5))      # Output: b'\x00\x00\x00\x00\x00'

# chr() - returns character from ASCII value
print("chr():", chr(65))         # Output: A

# dir() - returns list of attributes/methods
print("dir(list):", [x for x in dir(list) if not x.startswith('_')][:5])

# mod() - modulus operator (using % operator)
print("mod:", 10 % 3)           # Output: 1

# exec() - executes dynamically created code
exec("print('exec() works!')")

# format() - formats a value
print("format():", format(3.14159, ".2f"))  # Output: 3.14

# hex() - converts integer to hexadecimal
print("hex():", hex(255))        # Output: 0xff

# ascii() - returns ascii representation
print("ascii():", ascii("Hello ₹"))  # Output: 'Hello \\u20b9'

# pow() - returns power
print("pow():", pow(2, 3))      # Output: 8

# sum() - returns sum of iterable
print("sum():", sum([1, 2, 3, 4]))  # Output: 10

# sorted() - returns sorted list
print("sorted():", sorted([3, 1, 2]))  # Output: [1, 2, 3]
