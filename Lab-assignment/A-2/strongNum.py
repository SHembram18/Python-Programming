# PROGRAM: To check an integer is strong or not
# FILE: strongNum.py
# CREATED BY: Santosh Hembram 
# DATED: 23-09-20

num = int(input("Enter an integer: "))

temp = num
sum =0
fact = 1

while(num!=0):

    dg = num % 10

    for i in range(1,dg+1):

        fact = fact * i
        
    sum = sum + fact

    num = num // 10
    fact = 1


if(sum==temp):

    print(temp,"is a strong number")

else:

    print(temp,"is not a strong number")
        
