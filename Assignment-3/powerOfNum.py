# To find x to the power of y, where x and y  will be inputted from the keyboard

num = int(input("Enter a positive integer: "))
expo = int(input("Enter exponent value: "))

power = 1

for i in range(1,expo+1):

    power = power * num

print(num,"power",expo,"= ",power)
