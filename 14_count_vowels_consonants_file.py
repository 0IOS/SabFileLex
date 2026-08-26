filename = input("Enter the filename: ")

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

with open(filename, 'r') as f:
    for line in f:
        for char in line:
            if char.isupper():
                uppercase = uppercase + 1
            elif char.islower():
                lowercase = lowercase + 1
            if char.lower() in 'aeiou' and char.isalpha():
                vowels = vowels + 1
            elif char.isalpha():
                consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)
