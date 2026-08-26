def count_vowels(string):
    count = 0
    for char in string:
        if char.lower() in 'aeiou':
            count = count + 1
    return count

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
