import math
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
s=(a+b+c)/2
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle is", ar)