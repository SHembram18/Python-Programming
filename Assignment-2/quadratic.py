# To compute the real roots of quadratic equation ax2+bx+c=0

a = int(input("Enter the coefficient of a: "))
b = int(input("Enter the coefficient of b: "))
c = int(input("Enter the coefficient of c: "))

d = (b*b)-4*a*c

if( (a==0) and (b==0) ):
    print("=============No Solution===============")
    
elif(a==0):
    print("===============ONE ROOT==================")
    root = -c/b
    print("root = ",root)

elif(d > 0):
    print("=========TWO DISTINCT REAL ROOTS EXISTS=========")
    root1 = ( -b + (d ** 0.5) ) / (2*a)
    root2 = ( -b - (d ** 0.5) ) / (2*a)

    print("root1 = %.2f and root2 = %.2f" %(root1,root2))
    
elif(d==0):
    print("=========TWO EQUAL AND REAL ROOTS EXISTS=========")
    
    root1 = root2 = -b/(2*a)
    print("root1=root2 = %.2f" %(root1))

elif(d<0):
    print("=========THERE IS NO REAL ROOT=========")
    
