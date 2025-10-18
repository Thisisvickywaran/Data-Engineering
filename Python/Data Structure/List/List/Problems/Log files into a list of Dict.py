log=[
    "2025-09-24 Vicky  2",
    "2025-10-20 Sathya 23",
    "2025-09-20 Deeepak 10",
    "2025-03-23 Sathish 14",
    "2025-05-10 Parthiban 65"
]

parsed=[]

for items in log:
    date,user,id=items.split()
    parsed.append({"date":date,"user":user,"id":id})

print(parsed)