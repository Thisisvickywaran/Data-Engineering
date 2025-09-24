

def is_phonenumberavailable(text):
    if len(text)!=12:
        return False
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    if text[2]!="-":
        return False
    for i in range(3,6):
        if not text[i].isdecimal():
            return False
    if text[6]!="-":
        return False
    for i in range(7,12):
        if not text[i].isdecimal():
            return False
    return True


message= "is my number 91-978-089685 , and this is my brothers number 91-984-1006147"

for i in range(len(message)):
    text=message[i:i+12]
    if is_phonenumberavailable(text):
        print("phone number:"+text)
print("done")

