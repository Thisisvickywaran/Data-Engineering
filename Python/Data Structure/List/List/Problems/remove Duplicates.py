lst=[2,4,5,5,6,90,77,4,90,103]
unique=[]

for num in lst:
    if num not in unique:
        unique.append(num)

print(unique)