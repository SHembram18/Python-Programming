# Find multiplication table of number n

num = int(input("Enter a number: "))

for i in range(1,11):

    mul = num * i
    print(num," * ",i," = ",mul)

