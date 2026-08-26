filename = input("Enter the filename: ")
word = input("Enter the word to search: ")

count = 0
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        for w in words:
            if w == word:
                count = count + 1

if count > 0:
    print("The word '" + word + "' is found", count, "times in the file.")
else:
    print("The word '" + word + "' is not found in the file.")
