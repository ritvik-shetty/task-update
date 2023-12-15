# 1)
# name=input("Name:")
# print("goodafternoon",name)

# 2)
letter='''Dear NAME,
You are selected.
Date:<|DATE|>
'''

name=input("Enter your name \n")
date=input("Enter Date \n")

newletter=letter.replace("NAME",name)
newletter=newletter.replace("<|DATE|>",date)

print(newletter)