import random

n = int(input("How many times do you want to roll the dice? "))
print("Rolling the dice", n, "times:")
for i in range(n):
    result = random.randint(1, 6)
    print("Roll", i + 1, ":", result)
