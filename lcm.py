a=int(input('enter a'))
b=int(input('enter b'))
i=b
while True:
    if i%a==0 and i%b==0:
        print(f"lcm of {a} and {b} is {i}")
        break
    i+=1
    
    
