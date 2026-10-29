#============================================================================

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)

#============================================================================

n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)

#============================================================================

n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)

#============================================================================

n = int(input("Enter n: "))

i = 0
while (2 ** i) <= (n ** 2):
    print(2 ** i, end=" ")
    i += 1

#============================================================================

n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)

#============================================================================

x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 1
sign = -1

for i in range(2, 2 * n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum = sum + sign * (x ** i) / fact
    sign *= -1

print("Cosine series =", sum)

#============================================================================

import math

n = int(input("Enter a number: "))
root = int(math.sqrt(n))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

if prime:
    print(root, "is Prime")
else:
    print(root, "is Not Prime")

#============================================================================

for i in range(3):
    for ch in ['A', 'B', 'C']:
        print(ch, end=" ")
    print()

#============================================================================

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#============================================================================

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#============================================================================

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#============================================================================

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
