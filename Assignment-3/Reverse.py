# Write a Program to reverse a number

num = int(input("Enter a numebr: "))

num1 = num
reverse = 0

while(num!=0):

    digit = num % 10;
    reverse = digit + ( reverse * 10)
    num = num // 10

print("Reverse of ",num1," is = ",reverse)
