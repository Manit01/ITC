import math

i=0
while(i<=345):
    angle = math.radians(i)
    sine = math.sin(angle)
    cosine = math.cos(angle)
    print(i,"---", round(sine, 4), round(cosine, 4))
    i = i+15