filename = input("Enter the filename: ")

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        words = line.split()
        print('#'.join(words))
