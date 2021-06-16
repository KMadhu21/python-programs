a=int(input('enter a'))
b=int(input("enter b"))
i=a
while True:
    if a%i==0 and b%i==0:
        print(f"GCD of {a} and {b} is {i}")
        break
    i+=-1
