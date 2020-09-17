# To check a number is a Perfect square or not

import math

num = int(input("Enter a number: "))

root = math.sqrt(num)

if( int(root + 0.5)**2 == num):
    print(num,"is a perfect sqaure")

else:
    print(num,"is not a perfect sqaure")
