# Write a program to check the number is Armstrong or not

num = int(input("Enter a number: "))

temp = num
sum = 0 

while(temp!=0):

    digit = temp % 10
    sum = sum + (digit * digit * digit)
    temp = temp // 10
    
if(num == sum):
    print(num," is an Armstrong number")
else:
    print(num," is not an Armstrong number")
