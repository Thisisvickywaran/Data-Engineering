lst=[2,5,7,8,99]
reverse_lst=[]
for i in range(len(lst)-1,-1,-1):
    reverse_lst.append(lst[i])

print(reverse_lst)

lst = [5,8,3,78,90]
reversed1=[]
for i in range(len(lst)-1,-1,-1):
    reversed1.append(lst[i])

print(reversed1)


lst="Vigneshwaran"
print(lst)
reversed1=[]
for i in range(len(lst)-1,-1,-1):
    reversed1.append(lst[i])

print(reversed1)

reversed1="".join(reversed1)

print(reversed1)