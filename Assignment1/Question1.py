def avg(a, b, c):
    d=(a+b+c)/3
    return(d)

lst =[]
for i in range(1,4):
    element = int(input(f"Enter Num{i}: "))
    lst.append(element)
    
print("Average = ", avg(lst[0], lst[1], lst[2]))