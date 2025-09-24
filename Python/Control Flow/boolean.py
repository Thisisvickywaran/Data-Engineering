
print(bool("Hi"))

print(bool(0))
print("*"*5)
print(bool(1))
print("*"*5)

email=""
phone="0176-123456"
username = ""

print(any([email, phone, username])) # this will gives True since one has a value (Phone)
print(all([email, phone, username]))# this will gives False since two has a no value (email) (username)
print("*"*5)
print(isinstance(123,int))
print(isinstance("123",int))

print(isinstance("123",str))
print("*"*5)
print("hello".startswith("h"))
print("hello".startswith("e"))
print("hello".endswith("o"))