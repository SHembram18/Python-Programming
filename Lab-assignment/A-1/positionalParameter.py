# PROGRAM : To accept some inputs of different types and print them using positional parameters format i.e. {}
# FILE : positionalParameter.py
# CREATED BY : Santosh Hembram
# DATED : 16-09-20

x = int(input("Enter an integer value: "))

y = float(input("Enter a float value: "))

z = (input("Enter a string: "))

print("============Printing using positional parameter=============")

print("x = {0}".format(x))

print("y = {0}".format(y))

print("z = {0}".format(z))


print(" ")
print("x = {0} and y = {1} and z = {2}".format(x,y,z))
