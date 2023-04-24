a = int(input("Enter Side 1: "))
b = int(input("Enter Side 2: "))
c = int(input("Enter Side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Yes")
else:
    print("No")