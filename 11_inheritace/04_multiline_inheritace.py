# from calendar import c


class person:
    country="india"

    def takebreth(self):
        print("i am brething.....")

class employe(person):
    comapny="google"

    def takebreth(self):
        print("i am brething....")

class programer(employe):
    compny="wipro"


p=person()
p.takebreth()
e=employe()
e.takebreth()
pr=programer()
pr.takebreth()
print(pr.country)

