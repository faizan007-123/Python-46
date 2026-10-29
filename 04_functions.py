#============================================================================

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))

#============================================================================

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))

#============================================================================

def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number =", greater(a, b))

#============================================================================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(is_prime(n))

#============================================================================

def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))
print("Area of circle =", area_circle(r))

#============================================================================

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

n = int(input("Enter n: "))
print("Sum =", sum_n(n))
