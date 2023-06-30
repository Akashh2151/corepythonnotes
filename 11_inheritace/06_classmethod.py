class employee:
    name="akash"
    selery=100
    location="pune"

    # def changeSalery(self,sal):
    #     self.__class__.selery=sal      classs selery kiva kahon as change karu shakto apn but class change nhi hot te onlyadd kart ani  te print kart


    @classmethod                   #class attrubute ne change hot kel me class attrunute la
    def changeSalery(cal,salery):
        cal.selery=salery
    






e=employee()
print(e.selery)
e.changeSalery(500)
print(e.selery)