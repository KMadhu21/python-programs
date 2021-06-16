import math
a=float(input('enter a'))
b=float(input('enter b'))
c=float(input('enter c'))
d=(b*b)-(4*a*c)
if(d>0):
    print('the roots are real and distinct')
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print("root1",root1,"\nroot2",root2)
elif(d==0):
    print("\nthe roots are real and equal")
    root1=-b/(2*a)
    root2=root1
    print("root1",root1,"\nroot2",root2)
else:
    print('the roots are imaginary')
