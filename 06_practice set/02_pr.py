num1 =int(input("enter your fst subject mark"))
num2 =int(input("enter your second subject mark"))
num3 =int(input("enter your thrd subject mark"))
if (num1<33 or num2<33 or num3<33):
    print("your persentage is less then 33 so your faile")
elif(num1+num2+num3)/3<40:
    print("your falie becoz is less then 40 ") 
else:
    print("congraset you are pass ")     
