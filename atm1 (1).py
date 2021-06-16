print("****welcome to SBI bank ATM****")
print("put you card")
print("1.Cash withdraw")
print("2.Balance enquiry")
print("3.change atm pin")
print("4.cash deposit")
n=int(input("enter the option"))
if n==1:
  print("enter the amount you want to withdraw")
  m=int(input(""))
  if m<50000:
    print("----------")
    h=input("(yes/No)")
    if h=='yes':
      print("enter your pin number ****")
      p=int(input(""))
      a=input("(yes/No)")
      if a=='yes':
        print("Do you want to print receipt")
        b=input("(yes/No)")
        if b=='yes':
          print("your request is being processed")
          print("Take the money and receipt")
          print("****Thank you visit again****")
        else:
          print("your request is being processed")
          print("Take the money ")
          print("****Thank you visit again****")
      else:
        print("Transaction failed")
        print("Take your card out")
    else:
      print("Transaction failed")
      print("Take your card out")
  else:
    print("you have to enter the ammount less than 50000")
    print("Try again")
elif n==2:
  print("enter your pin number ****")
  c=int(input(""))
  d=input("(yes/No)")
  if d=='yes':
    print("your balance is *******.**")
  else:
    print("Transaction failed")
    print("Take your card out")
elif n==3:
  print("enter your present atm pin number ****")
  e=int(input(""))
  print("enter the pin you want to create ****")
  f=int(input(""))
  if e==f:
    print("you cannot enter same pin number")
    print("Transaction failed")
  else:
    i=input("(yes/no)")
    if i=='yes':
      print("your pin is successfully changed")
      print("****Thank you visit again****")
    else:
      print("Transaction failed")
      print("please take your card out")
elif n==4:
  print("enter the account number to which you have to deposit money **** **** ****")
  q=int(input(""))
  print("reconfirm account number")
  w=int(input(""))
  if q==w:
    j=input("(yes/No)")
    if j=='yes':
      print("enter the amount")
      u=int(input(""))
      r=input("(yes/No)")
      if r=='yes':
        print("your deposit is successfully completed")
        print("***Thank you vist again***")
      else:
        print("Transaction failed")
        print("Retry again")
    else:
      print("Transaction failed")
      print("Retry again")
  else:
    print("account number and reconfirm account number not matched")
    print("Transaction failed")
else:
  print("invalid option")

       
      
  
  
    
  
     
    
  