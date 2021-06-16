y=int(input("year"))
if((y%4==0)or(y%100==0)or(y%400==0)):
  print("leap year")
else:
  print("not leap year")