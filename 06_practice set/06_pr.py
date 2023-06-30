mark =int(input("enter your mark\n:"))
if mark>90:
    gred= "Ex"
elif mark>80:
    gred= "A"  
elif mark>70:
    gred= "b"   
elif mark>60:
    gred= "c"  
elif mark>50:
    gred= "d"   
else:
    gred=("your fali sorry try again letter")

print("your grade is:"+gred)