# 7 Write a Python program that accept string from user and perform following operations- i. Calculate length of string ii. Reverse the string

string_val = input("Enter a string: ")

# i. Calculate length of string
length = 0
for char in string_val:
    length += 1
print("Length of string:", length)

# ii. Reverse the string
rev_string = ""
for i in range(length - 1, -1, -1):
    rev_string += string_val[i]
print("Reversed string:", rev_string)
