# Program: To accept some inputs of different types and print the values with their type
# File: inputTypes.py
# Created By: Santosh Hembram
# Dated: 16-09-20

a = int(input("Enter an integer value: "))
b = float(input("Enter an float value: "))
c = input("Enter a string: ")

print("=============Printing the values with their type==============")

print("Type:",type(a),end=' ')
print(a)


print("Type:",type(b),end=' ')
print(b)


print("Type:",type(c),end=' ')
print(c)
