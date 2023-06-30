class employee:
    company="google"
    seleryy=100000
     
    def __init__(self,name,company,selery):
        self.name=name
        self.company=company
        self.selery=selery
        print("employee is created!") 

    def getdetels(self):
        print(f"the name of employe is{self.name}")  
        print(f"the company of employe is{self.company}")  
        print(f"the selery of employe is{self.selery}")  
    
    def getselery(self): #self mhanje khali object banavl aahe tech argument aahe
        print(f"this employee is working on: {self.company}\nselery is{self.seleryy}")
    
    # @staticmethod   #staticmethod vapraych karan as aahe ki self nhi lavl tari chalty nhitr te error thro kart one argument are mesing
    # def greet():
    #     print("good moring,akashsir!")
   
    # @staticmethod   #staticmethod vapraych karan as aahe ki self nhi lavl tari chalty nhitr te error thro kart one argument are mesing
    # def time():
    #     print("time is 9 am in moring!")

akash=employee("akash",100,"youtube")
# akash.getselery("thanks")      akash.getselery(akash)  self  mhanjech akash 
# akash.getdetels()
# akash.greet()
akash.getselery()
# akash.time() 