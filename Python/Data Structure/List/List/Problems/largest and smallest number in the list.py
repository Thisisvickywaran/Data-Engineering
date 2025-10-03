lst=[7,8,45,78,96,100]
max_lst=lst[0]
min_lst=lst[0]

for i in range(len(lst)):
    if lst[i] > max_lst:
        max_lst = lst[i]
    if lst[i] < min_lst:
        min_lst = lst[i]

print ("Maximum number in the list is ",max_lst)
print ("Minimum number in the list is ",min_lst)