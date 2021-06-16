a=int(input('enter a'))
b=int(input('enter b'))
if a>b:
    a,b=b,a
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        print("gcd of",a,'and',b,"is",i)
        break
