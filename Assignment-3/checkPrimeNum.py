# To check a number is prime or not

num = int(input("Enter a number: "))

check = 0

if(num>=0):
        for i in range(1,num+1):

                if( (num % i) == 0 ):
                    check=check+1

        if(check==2):
                print(num,"is a prime number.")

        else:
                print(num,"is not a prime number.");

else:
        print("========Please Enter a positive number=======")

