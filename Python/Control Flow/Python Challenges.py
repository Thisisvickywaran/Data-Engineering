
#Check if users's name is not empty and the age is greater than or equal to 8

user="vicky"
age =10

print(len(user)!=0 and age > 18)

print("check if the password is at least 8 characters long and does not contain spaces")

password="Vicky@2903"

password1="Vicky @2903"

print(" valid password " if len(password) > 8 and " " not in (password) else "invalid password")
print(" valid password " if len(password1) > 8 and " " not in (password1) else "invalid password")

print("check if a users email is not empty, contains '@' and ends with .com ")

user_email="vickywaran2903@gmail.com"
user_email1="vickywaran2903gmail.com"

print("Valid email" if len(user_email) != 0 and "@" in user_email and user_email.endswith(".com") else "Invalid email")


print("Valid email" if len(user_email1) !=0 and "@" in user_email1 and user_email1.endswith(".com") else "Invalid email")


