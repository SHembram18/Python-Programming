# PROGRAM: To find largest among three integer values, given as input
# FILE: largestThree.py
# CREATED BY: Santosh Hembram
# DATED: 16-09-20

num1 = int(input("Enter an integer value: "))
num2 = int(input("Enter an integer value: "))
num3 = int(input("Enter an integer value: "))

if(num1<num2):
    if(num2>num3):
        print(num2,"is the largest.")
    else:
        print(num3,"is the largest.")
else:
    if(num1>num3):
        print(num1,"is the largest.")
    else:
        print(num3,
              "is the largest.")
