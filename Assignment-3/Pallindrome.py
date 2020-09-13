# Check a number is pallindrome or not

num = int(input("Enter an integer: "))

rev = 0

num1 = num

while(num!=0):
    
    dg = num % 10
    rev = dg + (rev * 10)
    num = num // 10

if(rev == num1):
    print(num1," is a pallimdrome")

else:
    print(num1," is not a pallindrome");
    
