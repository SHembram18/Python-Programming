# To calculate the gross salary of an employee.

Basic = int(input("Enter the basic salary:- "))

DA = (Basic * 60) / 100

HRA = (Basic * 15) / 100

Conveyance = (Basic * 15) / 100

Medical = (Basic * 10) / 100

print("DA = ",DA)
print("HRA = ",HRA)
print("COnveyance = ",Conveyance)
print("Medical = ",Medical)

Gross_salary = Basic + DA + HRA + Conveyance + Medical

print("Gross salary = ",Gross_salary)
