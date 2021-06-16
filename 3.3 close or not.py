#close or not close
print("enter 2 numbers")
a=float(input("num1"))
b=float(input("num2"))
if a+0.001==b:
    print("close")
elif b+0.001==a:
    print("close")
else:
    print(" not close")
