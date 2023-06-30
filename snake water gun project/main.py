import random

#sanke water gun 
def gamewin(comp,you):
   
#com and you chose same to game are tie  
    if comp==you:
        return None

#check all posibility when computer chose s
    elif comp=='s':
        if you=='w':
           return False
        elif you=='g':
           return True
#check all posibility when computer chose w               
    elif comp=='w':
        if you=='g':
          return False
        elif you=='s':
          return True 
#check all posibility when computer chose g               
    elif comp=='g':
      if you=='s':
        return False
      elif you=='w':
           return True              


    print("comp turn: snake(s) water(w) or gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp='snake'
elif randno==2:
    comp='water'
elif randno==3:
    comp='gun'


# print(randno)
you =input("player's: snake(s) water(w) or gun(g)? ")
a=gamewin(comp,you)


if a == None:
  print("the game is tie")
elif a:
  print("you are win")
else :
  print("youlose")

print(f"computer chose: {comp}")
print(f"you chose: {you}")
 

 