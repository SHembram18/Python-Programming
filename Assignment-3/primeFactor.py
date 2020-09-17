# Print all the prime factors of a given number

num = int(input("Enter a number: "))
isPrime = 0

for i in range(2,num+1):

    if(num%i==0):
        isPrime = 1

    for j in range( 2,(i//2+1) ):
        
        if(i%j==0):
            isPrime = 0
            break


    if(isPrime==1):
        print(i,end=' ')
    
