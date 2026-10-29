#============================================================================

f = open("student.txt", "w")

f.write("Name: Atharv\n")
f.write("Roll Number: 101\n")
f.write("Branch: CSE\n")
f.write("Semester: 5\n")

f.close()

print("Student details written successfully.")

#============================================================================

f = open("student.txt", "r")

data = f.read()
print(data)

f.close()

#============================================================================

f = open("student.txt", "a")

f.write("College: DY Patil College\n")
f.write("City: Kolhapur\n")

f.close()

print("Information appended successfully.")

#============================================================================

f = open("student.txt", "r")

for line in f:
    print(line, end="")

f.close()

#============================================================================

f = open("student.txt", "r")

count = 0

for line in f:
    count += 1

print("Total number of lines:", count)

f.close()

#============================================================================

f = open("student.txt", "r")

data = f.read()
words = data.split()

print("Total number of words:", len(words))

f.close()

#============================================================================

f = open("student.txt", "r")

data = f.read()

print("Total number of characters:", len(data))

f.close()

#============================================================================

f = open("student.txt", "r")

lines = f.readlines()

for line in reversed(lines):
    print(line, end="")

f.close()
