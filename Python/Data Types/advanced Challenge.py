Text="968-Maria,( d@t@ Engineer );;27y  "

Text1 = Text.replace("@","a").strip()

name = Text[4:9] #Maria
 
text2=Text1[12:25]

print(text2)
role=text2.lower()#role

age=Text1[-3:]
print(age)


print(f"name: {name} role:{role} age:{age}")



