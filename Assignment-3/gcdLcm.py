# To find GCD and LCM of two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

i=1

while( (i<=num1) and (i<=num2) ):
    
    if( (num1%i==0) and (num2%i==0) ):
        GCD = i;
        
    i = i+1

print("The GCD of",num1,"and",num2,"is:",GCD)

lcm = (num1 * num2) // GCD
print("The LCM of",num1,"and",num2,"is:",lcm)
    
