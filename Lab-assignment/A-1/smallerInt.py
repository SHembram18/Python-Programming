# PROGRAM: To accept two integer as input and print the smaller using ternary operator syntax
# FILE: smallerInt.py
# CREATED BY: Santosh Hembram
# DATED: 16-09-20

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))

print("num1 = ",num1)
print("num2 = ",num2)

small = num1 if num1 < num2 else num2

print("The small number is: ",small)

