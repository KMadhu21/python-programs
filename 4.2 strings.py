#strings
a=input("enter a name")
b=input("enter a name")
c=len(a)
d=len(b)
if c==d:
  for i in range(c):
    print("{}{}".format(a[i],b[i]),end='')
else:
  print("the length of two strings are not same")