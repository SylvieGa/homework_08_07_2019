"""
Homework 7.3: Calculator
Write a program that does the basic arithmetic operations:
addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
"""


x = int(input("Enter something for x: "))

y = int(input("Enter something for y: "))

operation = input("Choose an operation (+, -, *, /: ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Flase operation")