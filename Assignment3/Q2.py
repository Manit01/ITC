Name = input("Enter Name: ")
try:
    SID = int(input("Enter SID: "))
except:
    print("Error: Enter Integral Vaule")
Department = input("Enter Department Name: ")
try:
    CGPA = float(input("Enter CGPA: "))
except:
    print("Error: Enter Float Vaule")
print(f"\nHey,{Name} Here!\nMy SID is {SID}\nI am from {Department} department and my CGPA is {CGPA}")