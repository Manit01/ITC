import random

for i in range(0,10,1):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(f"Question {i+1}: {a} x {b} = ", end="")
    intx = int(input())
    if intx == a*b:
        print("Right!")
    else:
        print("Wrong. The answer is ", a*b)