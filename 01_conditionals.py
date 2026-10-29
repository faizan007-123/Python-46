#============================================================================

n = int(input("Enter a number: "))

if n == 0:
    print("Number is Zero")
else:
    print("Number is Non-Zero")

#============================================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

#============================================================================

n = int(input("Enter a number: "))

if n >= 0:
    print("Positive Number")
else:
    print("Negative Number")

#============================================================================

ch = input("Enter a character: ")

if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")

#============================================================================

per = float(input("Enter Percentage: "))

if per >= 90:
    print("Excellent Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print("Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")

#============================================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

#============================================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest =", a)
elif b <= a and b <= c:
    print("Smallest =", b)
else:
    print("Smallest =", c)

#============================================================================

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#============================================================================

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#============================================================================

marital = input("Married or Unmarried (M/U): ")
gender = input("Gender (Male/Female): ")
age = int(input("Enter Age: "))

if marital == "M":
    print("Driver is Insured")
elif marital == "U":
    if gender == "Male" and age > 30:
        print("Driver is Insured")
    elif gender == "Female" and age > 25:
        print("Driver is Insured")
    else:
        print("Driver is Not Insured")
else:
    print("Invalid Input")
