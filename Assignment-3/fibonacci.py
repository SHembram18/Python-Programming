# To display all the fibonacci series upto nth number

num  = int(input("Enter the range: "))

f1 = 0
f2 = 1

if((num<0) or (num==0)):
    print("========Invalid range===============")

else:
    
    if(num==1):
        print(f1)
        
    else:

        print("========Displaying the fibonacci series upto",num,"th number========")
        print(f1)
        print(f2)
        for i in range(1,num-1):
        
            temp = f1 + f2
            f1 = f2
            f2 = temp
            print(temp)
    



