# PROGRAM: To find the GCD of any two integer and print the result slong with input value
# FILE: gcd.py
# CREATED BY: Santosh Hembram
# DATED: 23-09-20

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

i=1

while( (i<=num1) and (i<=num2) ):
    
    if( (num1%i==0) and (num2%i==0) ):
        GCD = i;

    i = i+1

print("The GCD of",num1,"and",num2,"is:",GCD)
        
