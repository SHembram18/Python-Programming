 # PROGRAM: To find the perimeter and area of a circle where, the diameter of the circle is given as input 
# FILE: circlePeriArea.py
# CREATED BY: Santosh Hembram
# DATED: 16-09-20

import math

D = float(input("Enter the Diameter of the circle(in cms): "))

peri = math.pi * D

r = D/2

area = math.pi * (r * r)

print("Perimeter = %.5f" %peri,"cm") 
print("Area = %.5f" %area,"cm square") 

