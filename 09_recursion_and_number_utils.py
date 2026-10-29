#============================================================================

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def binary(n):
    if n == 0:
        return ""
    return binary(n // 2) + str(n % 2)

#============================================================================

def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def palindrome(n):
    return str(n) == str(n)[::-1]


def armstrong(n):
    digits = str(n)
    total = 0

    for digit in digits:
        total += int(digit) ** len(digits)

    return total == n


def perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n
