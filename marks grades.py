n=int(input('enter marks'))
if (n<=100 and n>=80):
  print("A GRADE")
elif (n>=60 and n<80):
  print("B GRADE")
elif(n>=40 and n<60):
  print('C GRADE')
elif n>100:
	print('invalid marks')
else:
  print('FAIL')