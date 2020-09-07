# To round a floating point number to integer by considering
# the floor and ceiling operation without using built in function.

num = float(input("Enter a float number: "))
print("Before Rounding the number is: ",num)
if(num > 0):
    num = int(num + 0.5)
    print("After Rounding the number is: ",num)
else:
    num = int(num - 0.5)
    print("After Rounding the number is: ",num)
