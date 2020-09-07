# Calculate the hours, minutes, and seconds by giving second as input

sec = int(input("Enter the time in seconds:- "))

Hr = sec//3600

temp = Hr * 3600

sec = sec - temp

Min = sec//60

temp = Min * 60

sec = sec - temp 

print(Hr,'Hr:',Min,"Min:",sec,"sec")
