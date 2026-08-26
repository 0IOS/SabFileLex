source_file = input("Enter the source filename: ")
dest_file = input("Enter the destination filename: ")

with open(source_file, 'r') as f:
    lines = f.readlines()

with open(dest_file, 'w') as f:
    for line in lines:
        if 'a' not in line:
            f.write(line)

print("Done! Lines containing 'a' have been removed.")
print("Result written to", dest_file)
