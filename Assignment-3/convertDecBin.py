# To convert a Decimal number to its binary

num = int(input("Enter a Decimal number: "))

binary = 0
count = 0
num1 = num

if(num<0):
    print("======Enter a positve number========")

else:
    
    while(num!=0):

        rem = num%2
        c = pow(10,count)
        binary = binary + (rem * c)
        num = num // 2
        count = count + 1

print("The binary of ",num1,"is = ",binary)
