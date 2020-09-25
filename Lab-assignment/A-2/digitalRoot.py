# PROGRAM: To find the digital root of an integer
# FILE: digitalRoot.py
# CREATED BY: Santosh Hembram
# DATED: 23-09-20

num = int(input("Enter an integer: "))

temp = num
sum = 10

while(sum>=10):
    sum = 0

    while(num!=0):
    
        dg = num % 10
        sum = sum + dg
        num = num // 10

    num = sum 

   
print("The digital root of ",temp,"is",sum)

     
