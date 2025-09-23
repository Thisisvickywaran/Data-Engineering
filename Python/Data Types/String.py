
name = "Vicky"
print(type(name))

age = 28
print(type(age))
print("your age is :"+str(age))

# math

print(len(name))
password = "y@2903"

if (len(password) < 8):
    print("your password is shorter than 8 letters Please give a larger password")
else:
    print("Password is more than 8")

# give a count of the substring ( how many times the particular word is repeated)

text = """
Python is easy to learn
Python is powerful 
many people love Python"""

print(text.count("is"))

print(text.count("Python"))

# transmoration
# repalce
date = "29/03/1997"
print(date.replace("/", "-"))
print(date.replace("/", " "))

prive = "$1200.99"
print(prive)
print(prive.replace("$", "").replace(",", ""))  # replacing two thing at a time

# PCfor string

number = "+49 (176) 123-4567"  # take all the space and brackets

print(number.replace("+", "").replace(" ",
      "").replace("(", "").replace(")", "").replace("-", ""))

first_name = "vicky"
second_name = "waran"
print(first_name+"-"+second_name)

Folder = "C:/Users/vicky/"
file = "report.csv"
full_filepath = Folder+file
print(full_filepath)


a = 28
b = "Vicky"

print("a value is"+str(a)+"b value is "+b)  # needed a type cast

# f string is used for not changing the types of datatype while printing them with string , with this everything will be string
print(f"a value is {a} and b value is {b} ")


print(f"{{This is me inside a bracket}}")

# split the string
detail = "Vicky-29-India"
Splited_detail = detail.split('-')
print(Splited_detail)

stamp = "2025-09-20 14:30"
print(stamp.split(" "))

stamp = "2025-09-20"
print(stamp.split("-"))

# repeating the sstring

comment = "ha"
print(comment*3)

star = "*"
print(star*30)
print("-"*20)


# Indexing and slicing

a = "helloisworldbut"
print(a[0])
print(a[3])
print(a[-4])

print(a[0:4])
print(a[2:])

print(a[0::2])

print(a[-1])

# Cleaning
# Removing the white space from letf and right

text = " ###this is #enginerring webiste used for #general # purpose###    "
print(text)

print(text.lstrip())
print(text.rstrip())
print(text.strip())


text = "###sample #sentence###"
# removes only yhe # from the right and left side of the string
print(text.strip("#"))

# Strip will be really easy when we count the lenght of the string with white space in ti , this is used in data cleaning


text = "  Engineering"
print(len(text))

# lenght of the text becames lesser after the strip so it will helpful
print(len(text.strip()))

no_of_space = (len(text)) - (len(text.strip()))

print("Number of Spaces is", no_of_space)
clean = (len(text)) == (len(text.strip()))

print("is my data is clean?", clean)


# case Conversion

text = "python PROGRAMMING"
print(text.upper())
print(text.lower())

# cleaning the data with lower and stip methoods so that value can be same , always trim nad lowercase your data before matching them

search = 'Email  '.lower().strip()
data = 'email'.lower().strip()

print(search == data)

# searching

date = "2025-March-29"

print(date.startswith("2025"))

print(date.endswith("29"))


print("*"*5)

print("Month checking")
print('March' in date)

print("Document checking")
file = "resume.csv"
print(file.endswith(".csv"))
print(file.endswith(".docx"))

# check for the api endpoint


print("URL checking")
url = "https://api.compnay.com/v1/data"

print("/api" in url)


# find statement here we are finsing the - for skipping th country code and start the phone number

phone1 = "+91-9789-8908964"
phone2 = "91-9789-89-896"
phone3 = "00045-9789-89065"

print(phone1.find("-")) # this will give the position of the "-" in phone1

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])


#validate

country="USA"

number1="21234"
print(country.isalpha()) # check for the all the String is text
print(country.isnumeric())# check for the all the Number in text

print(number1.isnumeric())
print(number1.isdigit())



