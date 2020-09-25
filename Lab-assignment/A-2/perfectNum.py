# PROGRAM: To check a number is perfect or not
# FILE: perfectNum.py
# CREATED BY: Santosh Hembram
# DATED: 23-09-20

num = int(input("Enter an integer: "))

temp = num
sum = 0

for i in range(1,num):

    if(num%i==0):
        sum = sum + i

if(temp==sum):
    print(temp,"is a pefect number")
else:
    print(temp,"is not a perfect number")


    

    

