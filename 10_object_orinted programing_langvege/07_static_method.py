class employee:
    company="google"
    seleryy=100000
   
   
    def getselery(self): #self mhanje khali object banavl aahe tech argument aahe
        print(f"this employee is working on: {self.company}\nselery is{self.seleryy}")
    
    @staticmethod   #staticmethod vapraych karan as aahe ki self nhi lavl tari chalty nhitr te error thro kart one argument are mesing
    def greet():
        print("good moring,akashsir!")
   
    @staticmethod   #staticmethod vapraych karan as aahe ki self nhi lavl tari chalty nhitr te error thro kart one argument are mesing
    def time():
        print("time is 9 am in moring!")

akash=employee()
# akash.getselery("thanks")      akash.getselery(akash)  self  mhanjech akash 

akash.greet()
akash.getselery()
akash.time()