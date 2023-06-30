class employee:
    company="google"
    seleryy=100000
    def getselery(self): #self mhanje khali object banavl aahe tech argument aahe
        print(f"this employee is working on: {self.company}\nselery is{self.seleryy}")


akash=employee()
# akash.getselery() ,  akash.getselery(akash)  self  mhanjech akash 
akash.getselery()