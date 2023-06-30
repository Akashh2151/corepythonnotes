# ❤❤❤❤❤ factorial ky ast n= 1*2*3*4.....*n
# n=5
# product=1
# for i in range(n):
#     product=product*(i+1)
# print(product)




def factorial_iter(n): #iter mhanje iteretive fectorial method je loopcha madhatine factorial kadt 
    product=1           #defalute value set keli aahe product chi 1
    for i in range(n):   #
        product=product*(i+1)
    return product

def factorial_recursive(n):    #
    if n==1 or n==0:            #base condition use keli karan to khali formula use kely to - madhe hot aahe kami hot aahe so base condition are use  
        return 1
    return n * factorial_recursive(n-1)    
f=factorial_iter
f=factorial_recursive(1)
print(f)
        

