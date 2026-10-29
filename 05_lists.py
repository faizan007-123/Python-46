#============================================================================

fruits = ["Appke", "Mango", "Banana", "Orange", "Grapes"]

print(fruits)

#============================================================================

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[4])
print("Third element:", numbers[2])

#============================================================================

colors = ["Red", "Blue", "Green", "Yellow"]

colors[2] = "Pink"

print(colors)

#============================================================================

numbers = [10, 20, 30]

numbers.append(40)       
numbers.insert(0, 5)  
numbers.insert(2, 15)    

print(numbers)

#============================================================================

students = ["Riya", "Amit", "Neha", "Rahul", "Pooja"]

students.pop(0)          
students.pop()           
students.remove("Neha")  

print(students)

#============================================================================

numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

total = sum(numbers)
average = total / 10

print("Sum:", total)
print("Average:", average)

#============================================================================



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

#============================================================================

cities = ["Pune", "Mumbai", "Delhi", "Nashik", "Nagpur"]

city = input("Enter city name: ")

if city in cities:
    print("City found")
else:
    print("City not found")

#============================================================================

numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print(reversed_list)

#============================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5:", numbers[:5])
print("Last 5:", numbers[5:])
print("Middle 4:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])
