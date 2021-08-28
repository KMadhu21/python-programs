#3.3
#a=float(input('enter a')) 
##b=float(input('enter b'))
##if a>b:
##    c=a-b
##else:
##    c=b-a
##if c<=0.001:
##    print('close')
##else:
##    print("not close")

# 4.1
#n=input('enter')
##for i in n:
##    if i in 'aeiouAEIOU':
##        print(i)


# 4.2
#a=input('enter') 
##b=input('enter')
##if (len(a)!=len(b)):
##    print("lenghts are not same")
##else:
##    for i in range(len(a)):
##        print("{}{}".format(a[i],b[i]),end='')

#4.3
#n=int(input('enter')) 
##print("{:,}".format(n))

##a=input('enter')  4.4
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


#5.1
#import random 
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


# 5.2
#n=int(input('enter'))
##a=[]
##for i in range(1,n+1):
##    if n%i==0:
##        a.append(i)
##print(a)

#5.3
#import random 
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


#6.1
##n=list(map(int,input().split())) 
##print(n)
##a=set(n)
##b=list(a)
##print(b)


#6.2
##units=['inches','yards','miles','millimeters','centimeters','metre','kilometer'] 
##cf=[12,0.33333,0.000189393939,304.8,30.48,0.0003048]
##f=float(input('enter the lenth in feets'))
##for i in range(len(units)):
##    print(f'enter {i+1} to covert feets to {units[i]}')
##i=int(input('enter ur choice'))-1
##print(f'length in {units[i]}={f*cf[i]}')


 #7.1
##def sum_digits(n): 
##    s=0
##    while(n!=0):
##        r=n%10
##        s=s+r
##        n=n//10
##    return s
##n=int(input('enter n'))
##a=sum_digits(n)
##print(a)

##7.2
##def first_diff(a,b):
##    m=max(len(a),len(b))
##    for i in range(m):
##        if i>=len(a) or i>=len(b):
##            return i
##        if a[i]!=b[i]:
##            return i
##    return -1
##a=input('enter')
##b=input('enter')
##c=first_diff(a,b)
##print(c)

##7.3
##def number_of_factors(n):
##    c=0
##    for i in range(1,n+1):
##        if n%i==0:
##            c+=1
##    return c
##n=int(input('enter n'))
##a=number_of_factors(n)
##print(a)

#7.4
##def is_sorted(n):
##    if n[0]==max(n):
##        for i in range(len(n)-1):
##            if(n[i]<n[i+1]):
##                return False
##            else:
##                return True
##        
##    elif n[0]==min(n):
##        for i in range(len(n)-1):
##            if(n[i]<n[i+1]):
##                return False
##            else:
##                return True
##    else:
##            return False
##
##n=list(map(int,input().split()))
##a=is_sorted(n)
##print(a)
##            





















