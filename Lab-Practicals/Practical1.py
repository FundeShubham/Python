# 1 Write program in Python to read a list of N numbers from the user; compute and display the maximum in list, minimum in list, sum of all numbers in the list and average of numbers.

n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = float(input("Enter number: "))
    numbers.append(num)

if n > 0:
    max_num = numbers[0]
    min_num = numbers[0]
    total_sum = 0
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        total_sum += num
        
    average = total_sum / n
    
    print("Maximum in list:", max_num)
    print("Minimum in list:", min_num)
    print("Sum of all numbers:", total_sum)
    print("Average of numbers:", average)
else:
    print("List is empty.")
