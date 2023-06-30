

class person:
    country="india"

    def __init__(self):
        super().__init__()
        print("intilzing person....")

    def takebreth(self):
        print("i am brething.....")
         

class employe(person):
    comapny="google"

    def __init__(self):                  #apn super(). la init so bat pn vapru shakto aata second number cha class print kel aahe tari pn te super method vaprya mule te varcha class pn ghety
        super().__init__()
        print("intilzing employee....")

    def takebreth(self):
        # super().takebreth()     
        print("i am brething....")

class programer(employe):
    compny="wipro"

    def takebreth(self):
        # super().takebreth()                    #super() he tyacha varcha super class pahil run kart ani parat sothach kart tyamule aplya la te donda dist
        print("programer is brething....")


# p=person()
# p.takebreth()
e=employe()
# e.takebreth()
# pr=programer()
# pr.takebreth()
# print(pr.country)
