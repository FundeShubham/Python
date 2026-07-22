# 2 Write a program in Python to accept a number from the user and print digits of the number in a reverse order.

num = int(input("Enter a number: "))
print("Digits in reverse order:", end=" ")

while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num = num // 10
print()
