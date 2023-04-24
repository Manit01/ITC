list = []
def greatest(a,b,c):
    if(a==b==c):
        print("All Numbers are Equal")
    elif(a>b):
        if(a>c):
            print(f"{a} is Greatest")
        else:
            print(f"{c} is Greatest")
    elif(c>b):
        if(c>a):
            print(f"{c} is Greatest")
        else:
            print(f"{a} is Greatest")

for i in range(0,3,1):
    Number = int(input(f"Enter Number {i+1}: "))
    list.append(Number)
print(greatest(list[0],list[1],list[2]))