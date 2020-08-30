#PROGRAM    :- Find the area of triangle using three sides
#File       :- Area.py
#CREATED BY :- Sant0sh Hembram
#DATED      :- 29/08/20



a = 24
b = 30
c = 18

#Calculating the permimeter
s = ( a + b + c ) / 2

#Calculating the area
area =  ( s*(s-a)*(s-b)*(s-c) ) ** 0.5

print('The area of the triangle is : ',area)
