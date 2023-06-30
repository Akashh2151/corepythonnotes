num=int(input("enter your number:"))
priem=True
for a in range(2,num):
     if(num%a == 0):
         priem=False
         break
if priem:
     print("this is priem")
else:
    print("this is not prem")   
