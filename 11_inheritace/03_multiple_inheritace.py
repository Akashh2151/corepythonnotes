class employee:
    company="google"
    

class freelancer:
    company="google"
    level=0

    def upgrade(self):
        self.level=self.level+1


class programer(employee,freelancer):
    name="rohit"

p=programer()
p.upgrade()
print(p.level)
print(p.company)
