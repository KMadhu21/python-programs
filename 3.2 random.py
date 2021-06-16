#random number
import random
n=int(input("enter a number"))
a=random.randint(1,10)
print("random number is",a)
if n==a:
  print("Matched")
else:
  print("Not Matched")