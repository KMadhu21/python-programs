n=int(input("enter a number"))
temp=n
digits=0
while temp!=0:
    digits+=1
    temp=temp//10
temp=n
sum=0
while n!=0:
    r=n%10
    sum=sum+pow(r,digits)
    n=n//10
if temp==sum:
    print(temp,"is armstrong number")
else:
    print(temp,"is not a armstrong number")
                
