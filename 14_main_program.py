import recursive

n = int(input("Enter a number: "))

print("Factorial:", recursive.factorial(n))

print("Fibonacci:", end=" ")
for i in range(n):
    print(recursive.fibonacci(i), end=" ")

print()

print("Sum of digits:", recursive.sum_digits(n))

if n == 0:
    print("Binary: 0")
else:
    print("Binary:", recursive.binary(n))
