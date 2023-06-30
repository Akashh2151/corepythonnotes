text=(input("enter your text"))
# spam=False
if("akash desai is good boy" in text):
    spam=True
elif("prakash desai is good boy" in text):
    spam=True
elif("priti is good girl" in text):
    spam=True
elif("priti is tooper in yc collge" in text):
    spam=True
if(spam):
    print("this is spam")
else:
    print("this is not spam")    
    