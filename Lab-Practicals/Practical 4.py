# 4 Write Program in Python to accept student’s five courses’ marks, compute and display result and grade. Student is pass if he/she scores marks equal to and above 40 in each course. If student scores aggregate greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the grade if first division. If aggregate is 50>= and <60, then the grade is second division. If aggregate is 40>= and <50, then the grade is third division.

m1 = float(input("Enter marks for Course 1: "))
m2 = float(input("Enter marks for Course 2: "))
m3 = float(input("Enter marks for Course 3: "))
m4 = float(input("Enter marks for Course 4: "))
m5 = float(input("Enter marks for Course 5: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    print("Result: Pass")
    total_marks = m1 + m2 + m3 + m4 + m5
    aggregate = (total_marks / 500) * 100
    print("Aggregate:", aggregate, "%")
    
    if aggregate > 75:
        print("Grade: Distinction")
    elif aggregate >= 60 and aggregate < 75:
        print("Grade: First Division")
    elif aggregate >= 50 and aggregate < 60:
        print("Grade: Second Division")
    elif aggregate >= 40 and aggregate < 50:
        print("Grade: Third Division")
else:
    print("Result: Fail")
