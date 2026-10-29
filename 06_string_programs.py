#============================================================================

s = input("Enter a string: ")

count = 0
for ch in s:
    count += 1

print("Length:", count)

#============================================================================

s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

#============================================================================

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed string:", reverse)

#============================================================================

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#============================================================================

s = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in s:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)

#============================================================================

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("Result:", result)

#============================================================================

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("String without spaces:", result)

#============================================================================

s = input("Enter a string: ")
ch = input("Enter character to find: ")

count = 0

for c in s:
    if c == ch:
        count += 1

print("Frequency:", count)

#============================================================================

s = input("Enter a string: ")

if len(s) > 0:
    print("First character:", s[0])
    print("Last character:", s[-1])
else:
    print("String is empty")

#============================================================================

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))

#============================================================================

s = input("Enter a sentence: ")

words = s.split()

print("Total words:", len(words))

#============================================================================

s = input("Enter a sentence: ")

words = s.split()

if len(words) > 0:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)
else:
    print("No words found")

#============================================================================

s = input("Enter a sentence: ")

words = s.split()

if len(words) > 0:
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    print("Shortest word:", shortest)
else:
    print("No words found")

#============================================================================

s = input("Enter a sentence: ")

words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print("Title case:", result.strip())

#============================================================================

s = input("Enter a string: ")

duplicates = ""

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates += ch

print("Duplicate characters:", duplicates)

#============================================================================

import re

text = "a+b*c"
result = re.escape(text)

print(result)

#============================================================================

import re

text = "apple,banana,orange"
result = re.split(",", text)

print(result)

#============================================================================

import re

text = "I like playing cricket"
result = re.sub("cricket", "football", text)

print(result)

#============================================================================

import re
string = """My ticket Number is 1234567890 and my friend's ticket number is 7895641235"""

regex = '\d+'
matches = re.findall(regex, string)
print("All matches found:", matches)

#============================================================================

import re

text = "Python is easy to learn"
pattern = "easy"

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")

#============================================================================

import re

pattern = re.compile("Python")

text = "Python is easy to learn"

result = pattern.search(text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")

#============================================================================

def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count


def reverse_string(s):
    return s[::-1]


def palindrome(s):
    return s == s[::-1]


def count_words(s):
    return len(s.split())


def remove_spaces(s):
    return s.replace(" ", "")
