# To find sum of digits of a number

num = int(input("Enter a number: "))

if(num<0):
    print("=========Please enter a positive number=============")

elif(num<=9):
    print("=======You Enter a single digit number [sum of digits = ",num,"]==============")

else:

    sum = 0
    while(num!=0):
        
        temp = num % 10
        sum = sum + temp
        num = num // 10

    print("The sum of the digits = ",sum)
