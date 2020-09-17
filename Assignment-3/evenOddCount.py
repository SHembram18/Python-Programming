# To input 10 random numbers & find how many of them are even and odd

print("============You have to enter 10 random numbers===================")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
num7 = int(input("Enter a number: "))
num8 = int(input("Enter a number: "))
num9 = int(input("Enter a number: "))
num10 = int(input("Enter a number: "))

e_count = 0
o_count = 0

if(num1 % 2 == 0):
    e_count = e_count+1 

if(num2 % 2 == 0):
    e_count = e_count+1

if(num3 % 2 == 0):
    e_count = e_count+1

if(num4 % 2 == 0):
    e_count = e_count+1

if(num5 % 2 == 0):
    e_count = e_count+1

if(num6 % 2 == 0):
    e_count = e_count+1

if(num7 % 2 == 0):
    e_count = e_count+1

if(num8 % 2 == 0):
    e_count = e_count+1

if(num9 % 2 == 0):
    e_count = e_count+1

if(num10 % 2 == 0):
    e_count = e_count+1

o_count = 10 - e_count

print("Total no. of even = ",e_count)
print("Total no. of odd = ",o_count)
