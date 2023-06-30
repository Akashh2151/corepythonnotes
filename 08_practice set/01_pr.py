def maximum(num1,num2,num3):
    if(num1>num2):
       if(num1>num3):
           return num1
    else:
        return num3
    
    if(num2>num3):
        return num2
    else:
        return num3
m=maximum(23,34,56)
# print("gretest value is:"+str(m))        



def maximum(num1,num2,num3):
    if(num1<num2):
         if(num1<num3):
             return num1
         else:
             return num3
        
    if(num2<num3):
        return num2
    else:
        return num3
m=maximum(8,7,35)
print("your maximum number is:",m)                
