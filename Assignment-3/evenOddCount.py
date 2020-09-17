# To input 10 random numbers & find how many of them are even and odd

print("============You have to enter 10 random numbers===================")

even = 0
odd = 0

for i in range(1,11):
    
    num = int(input("Enter the number: "))
    
    if(num%2==0):
        even = even + 1
        
    else:
        odd = odd + 1

print("Total even no. = ",even)
print("Total odd no. = ",odd)

    
