mydisnary= {
    "fast":"in the quik maner",
     "akash":"akash is a coder",
     "mark":[1,2,3,4,5],
 "anothrdict":{'stan':'prakash'}    
}
# print(type(mydisnary.keys())) # type keych kont aahe te print show karych yach clas dic key aahe
# method dicnary 
print((mydisnary.keys())) # show kart keys la
print(mydisnary.values()) # print the value.....
print(mydisnary.items()) #print key and value all conttens 
print(mydisnary)
updatedisnary = {
    "rani":"nehabai",
    "akash":"prakash",
    "kakimami":"okikaki"


}
mydisnary.update(updatedisnary) #addig new key and value using update method
print(updatedisnary)
# .get error kashasathi use karych aahe
print(mydisnary.get("fast")) # .get funtion use karych karan mhanje te je value aahe tyalach ghettt
# print(mydisnary["fast22222"]) #same tasch kel aahe but .get funtion use nhi kel 2222 as lavl aahe mg te error throw kart
