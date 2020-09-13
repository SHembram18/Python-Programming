# Write a program to find sum of the natural number

num = int(input("Enter a number: "))

if(num < 0):
    print("============Enter a positive number============")

else:
    sum = 0
    while(num!=0):
        sum = (sum + num);
        num = num-1

    print("The sum is: ",sum)
