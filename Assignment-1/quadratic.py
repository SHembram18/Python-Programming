#finds roots of quadratic equation


a = 1
b = 7
c = 12

d = ( (b*b) - 4*a*c )

if d > 0:

    x1 = ( -b + (d ** 0.5) ) / (2*a)
    x2 = ( -b - (d ** 0.5) ) / (2*a)

    print('x1 = ',x1 , 'and' ,'x2 = ',x2)

elif d == 0:

    x1 = x2 = -b/(2*a)
    print('x1=x2 = ',x1)
    
else:

    print('d<0 so it is an imaginary roots')
    
