"""
Module 01
How should you systematically test this program?
"""

total = 0
number_of_people = 0
age = int(input("Age: "))
while age > 0:
    total = total + age
    number_of_people += 1
    age = int(input("Age: "))
average = total / number_of_people
print(f"Average age of {total} people is {average}")
