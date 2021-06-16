n=int(input('enter n'))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime number")
elif c==1:
    print("not a prime nor composite")
else:
    print("not a prime number")
