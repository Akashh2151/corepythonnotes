class calculator:
    def __init__(self,num):
        self.number=num
    
    def square(self):
        print(f"the value of{self.number} square is {self.number**2}")    
   
   
    def squareroot(self):
        print(f"the value of{self.number} square is {self.number**0.5}")    
   
    def cube(self):
        print(f"the value of{self.number} square is {self.number**3}")    


    @staticmethod 
    def greet():
        print("heelo sir, good moring\n")


a=calculator(3)
a.greet()
a.square()    
a.squareroot()    
a.cube()    