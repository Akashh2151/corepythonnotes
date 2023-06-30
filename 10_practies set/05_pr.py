class train():
    def __init__(self,name,seats,prize):
        self.name=name
        self.seats=seats
        self.prize=prize

    def getinfo1(self):
        print(f"name of train is: {self.name}")


    def getinfo2(self):
        print(f"number of sets is: {self.seats}")

    def getinfo3(self):
        print(f"seats prize is: {self.prize}")       


    def bookticket(self):
        if(self.seats>0):
            print(f"you train ticket is booked! {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"all ticket is full sorry vist next time:  {self.seats} ")       
    





akash=train("indian relivye",100,100)
akash.getinfo1()
akash.getinfo2()
akash.getinfo3()
akash.bookticket()
akash.bookticket()
akash.bookticket()
akash.bookticket()
