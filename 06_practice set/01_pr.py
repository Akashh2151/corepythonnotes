num1 =int(input("enter your fst number1: "))
num2 =int(input("enter your sec number2: "))
num3 =int(input("enter your thr number3: "))
num4 =int(input("enter your four number4: "))
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(str(f1)+"\ngreter")
else:
  print(str(f2)+"\ngreter")

