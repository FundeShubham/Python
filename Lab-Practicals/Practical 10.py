# 10 Write a Python program to find whether a particular element is present in the list using a loop.

n = int(input("Enter number of elements in the list: "))
elements = []
for i in range(n):
    val = input("Enter element: ")
    elements.append(val)

search_element = input("Enter the element to search for: ")

found = False
for item in elements:
    if item == search_element:
        found = True
        break

if found:
    print("Element", search_element, "is present in the list.")
else:
    print("Element", search_element, "is not present in the list.")
