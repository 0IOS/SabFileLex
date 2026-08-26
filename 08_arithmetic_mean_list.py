def arithmetic_mean(lst):
    total = sum(lst)
    mean = total / len(lst)
    return mean

n = int(input("How many elements do you want to enter? "))
lst = []
for i in range(n):
    num = float(input("Enter element: "))
    lst.append(num)

print("List:", lst)
print("Arithmetic Mean:", arithmetic_mean(lst))
