Gross_Income = int(input("Enter Gross Income: "))
No_of_Dependents = int(input("Enter Number of Dependents: "))

Taxable_Income = Gross_Income - 10000 - 3000*No_of_Dependents

if(Taxable_Income < 0):
    Tax = 0
    print(Tax)

else:
    Tax = Taxable_Income*0.2
    print(Tax)