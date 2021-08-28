##a=float(input('enter a'))
##b=float(input('enter b'))
##if a>b:
##    c=a-b
##else:
##    c=b-a
##if c<=0.001:
##    print('close')
##else:
##    print("not close")

##n=input('enter')
##for i in n:
##    if i in 'aeiouAEIOU':
##        print(i)


##a=input('enter')
##b=input('enter')
##if (len(a)!=len(b)):
##    print("lenghts are not same")
##else:
##    for i in range(len(a)):
##        print("{}{}".format(a[i],b[i]),end='')

##n=int(input('enter'))
##print("{:,}".format(n))

##a=input('enter')
##for i in range(len(a)-1):
##    if a[i].isdigit():
##        if a[i+1]!=")":
##            print(a[i],end='')
##            print('*',end='')
##        else:
##            print(a[i],end='')
##    else:
##        print(a[i],end='')
##if i==len(a)-2:
##    print(a[i+1],end='')


##import random
##a=[]
##n=int(input('enter'))
##c=0
##for i in range(n):
##    a.append(random.randint(1,100))
##print(a)
##s=0
##for i in a:
##    s=s+i
##    avg=s/n
##print("average is",avg)
##print('maximum is ',max(a))
##print('minimum is ',min(a))
##a.remove(max(a))
##a.remove(min(a))
##for i in a:
##    if i%2==0:
##        c+=1
##print('the no of even is',c)
##b=set(a)
##b=list(a)
##print('2 max is',max(b))
##print('2 min is',min(b))


##n=int(input('enter'))
##a=[]
##for i in range(1,n+1):
##    if n%i==0:
##        a.append(i)
##print(a)

##import random
##a=[]
##l=[]
##n=int(input('enter'))
##for i in range(n):
##      a.append(random.randint(0,1))
##print(a)
##c=1
##for i in range(len(a)-1):
##    if a[i]==a[i+1] and a[i]==0:
##        c+=1
##    else:
##        l.append(c)
##        c=1
##else:
##    l.append(c)
##print(max(l))


##n=list(map(int,input().split()))
##print(n)
##a=set(n)
##b=list(a)
##print(b)





