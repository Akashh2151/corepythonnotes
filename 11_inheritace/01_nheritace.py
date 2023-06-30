# from distutils.log import info

#this is base class 

class employe:
    compny="google"
    selery=20000

    def getinfo(self):
        print("employee is created")


# this is dreive class

class programer(employe):
    name="akash"


    def programerinfo(self):
          print(f"programer name is: {self.name}")

    def getinfo(self):
       print("programer is ceated")


e=employe()
e.getinfo()
p=programer()
p.getinfo()
print(e.selery)

   