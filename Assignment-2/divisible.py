# To test whether the given number is divisible by both 11 and 13
#   or by both 5 and 7

num = int(input("Enter a number:- "))

if( (num % 11 == 0) and (num % 13 == 0) ):
    print(num," is divisible by both 11 and 13")
    
else:
    print(num," is not divisble by 11 and 13")


if( (num % 5 == 0) and (num % 7 == 0)):
    print(num," is divisible by both 5 and 7")

else:
    print(num," is not divisible by 5 and 7")

    
