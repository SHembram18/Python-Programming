# Enter three numbers and arrange the numbers in descending order

num1 = int(input("Enter the 1st number:- "))
num2 = int(input("Enter the 2nd number:- "))
num3 = int(input("Enter the 3rd number:- "))

x1 = max(num1,num2,num3)
x3 = min(num1,num2,num3)

x2 = (num1 + num2 + num3)-x1-x3

print("Descending order: ",x1,x2,x3)
