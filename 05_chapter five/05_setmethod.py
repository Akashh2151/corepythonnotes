a =set()
print(type(a))

#ading a value
a.add(2)
a.add(3)
a.add(5)# dobel zal ki te ignor kart
a.add(5)
# b.add([8,7,9,6,8,7]) #apn list la add nhi kru shakat set madhe
# a.add[(9,8,7,6)] # list  apn nhi taku shakat nhi karn te hashebal nhi
# a.add({4:3}) # dishnary pn nhi add karu shaka apn 
a.add(6)
print(a)

#lenth of set kas kadych te aahe
print(len(a))


#remove kaise kare uske bare me he
a.remove(6)
print(a)
a.remove(5)
print(a)


# konta pn remove kart ik item
print(a.pop())
print(a)

# sagal emty kart set 
print(a.clear())
print(a)


