# To print the numbers in words

num = int(input("Enter a number: "))
rev = 0

while(num!=0):
    
    dg = num % 10
    rev =  dg+(rev*10)
    num = num // 10

while(rev!=0):
    
    dg1 = rev % 10

    if(dg1==0):
        x = "ZERO "
        
    elif(dg1==1):
        x = "ONE "
        
    elif(dg1==2):
        x = "TWO "

    elif(dg1==3):
        x = "THREE "

    elif(dg1==4):
        x = "FOUR "
        
    elif(dg1==5):
        x = "FIVE "

    elif(dg1==6):
        x = "SIX "

    elif(dg1==7):
        x = "SEVEN "
        
    elif(dg1==8):
        x = "EIGHT "

    elif(dg1==9):
        x = "NINE "

    rev = rev // 10
   
    print(x,end='')

    
