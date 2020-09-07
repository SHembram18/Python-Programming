# Temperature of an oven setting by reading from a pressure meter

r = int(input("Enter the reading:- "))

if( (r == 2) or (r == 3) ):
    print("Temperature set to 500 degrees.")
    
elif( r==4):
    print("Temperature set to 600 degrees.")

elif((r==5)or(r==6)or(r==7)):
    print("Temperature set to 700 degrees.")

elif((r<2) or (r>7)):
    print("DEFAULT:- The temperature setting is 300 degrees.")



