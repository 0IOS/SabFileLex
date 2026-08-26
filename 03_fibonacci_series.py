def fibonacci(n):
    a = 0
    b = 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

n = int(input("Enter the number of terms: "))
fibonacci(n)
