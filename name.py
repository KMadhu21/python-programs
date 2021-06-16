##name=input('')
##age=int(input(''))
##print(f' my name is {name} aged  {age}')

##def details():
##    name=input('enter name')
##    age=int(input('enter age '))
##    print(f'my name is {name} aged {age}')
##
##for i in range(1,5):
##    details()


def details(name,age):
    return(f'my name is {name} aged {age}')

x=input('enter name')
y=int(input('enter age '))
print(details(x,y))
