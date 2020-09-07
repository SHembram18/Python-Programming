# Input the mark of a student in three subjects
# Calculate the grade of the student

MIL = int(input("Enter the mark of 1st subject:- "))

ENG = int(input("Enter the mark of 2nd subject:- "))

TLS = int(input("Enter the mark of 3rd subject:- "))

total = MIL + ENG + TLS
print("Total mark secured: ",total)

avg = total / 3
print("Average = %.2f" %avg)

if( avg >= 90 ):
    print("Grade is: O")

elif( avg >= 80 ):
    print("Grade is: E")

elif( avg >= 70):
    print("Grade is: A")

elif( avg >= 60):
    print("Grade is: B")

elif(avg < 60):
    print("Grade is: C")
