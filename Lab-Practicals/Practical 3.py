# 3 Write Program in Python to calculate the salary of an employee given his Basic Pay. Let DA be 80% of Basic Pay, HRA be 10 % of basicpay and TA be 5% of basic pay. Calculate gross salary of employee. Professional tax is to be deducted from gross salary as 2% of gross salary. Calculate salary payable after deductions.

print("Welcome To Salary Calculator")
print("Please Enter Your Values Respecfully")

# Input: Basic Pay
basic_pay = float(input("Enter Basic Pay: "))

# Allowances
da = 0.80 * basic_pay   # Dearness Allowance
hra = 0.10 * basic_pay  # House Rent Allowance
ta = 0.05 * basic_pay   # Travel Allowance

# Gross Salary
gross_salary = basic_pay + da + hra + ta

# Professional Tax Deduction
professional_tax = 0.02 * gross_salary

# Net Salary (Salary Payable)
net_salary = gross_salary - professional_tax

# Output
print("\n--- Salary Details ---")
print("Basic Pay: Rs.", basic_pay)
print("Dearness Allowance (80%): Rs.", da)
print("House Rent Allowance (10%): Rs.", hra)
print("Travel Allowance (5%): Rs.", ta)
print("Gross Salary: Rs.", gross_salary)
print("Professional Tax (2%): Rs.", professional_tax)
print("Net Salary (After Tax): Rs.", net_salary)
print("\nThank you for using the Salary Calculator!")
