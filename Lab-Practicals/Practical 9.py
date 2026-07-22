# 9 Write a Python program that finds the sum of all the numbers in a list using a while loop.

n = int(input("Enter number of elements in the list: "))
numbers = []
i = 0
while i < n:
    num = float(input("Enter number: "))
    numbers.append(num)
    i += 1

total_sum = 0
index = 0
while index < len(numbers):
    total_sum += numbers[index]
    index += 1

print("Sum of all numbers in the list:", total_sum)
