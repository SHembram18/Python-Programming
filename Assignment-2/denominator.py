# To evaluate the following expression from inputted values of a,b,c,d.
# x = (a-b)/(c-d)

a = float(input("Enter a value:- "))
b = float(input("Enter a value:- "))
c = float(input("Enter a value:- "))
d = float(input("Enter a value:- "))

if( (c-d) == 0 ):
    print("==============CANNOT DIVIDE BY ZERO============== ")
else:
    x = ( (a-b)/(c-d) )
    print("RESULT = %.2f" %(x))
