# 6 Write a menu driven Python program using functions to perform calculator operations such as adding, subtracting, multiplying, and dividing two integers

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 5:
        print("Exiting calculator...")
        break
        
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    
    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please try again.")
