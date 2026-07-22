# 5 Write program in Python to check leap year. Write function with year as argument and return whether year is leap year or not.

def check_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

y = int(input("Enter a year: "))
if check_leap_year(y):
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")
