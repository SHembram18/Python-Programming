# PROGRAM : To accept some inputs of different types and print them using format specification e.g. %
# FILE : formatSpecificationPrint.py
# CREATED BY : Santosh Hembram
# DATED : 16-09-20
#

x = int(input("Enter an integer value: "))

y = float(input("Enter a float value: "))

z = str(input("Enter a string: "))

print("==============Printing using format specification =============")

print("x = %d and y = %.3f and z = %s" %(x,y,z))
