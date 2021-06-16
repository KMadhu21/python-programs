n=int(input("enter a number"))
sum=0
if n>0:
    while n!=0:
        r=n%10
        sum=sum+r
        n=n//10
    print(sum)
else:
    print("it is not a positive number")
