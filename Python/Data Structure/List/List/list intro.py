lst=[1,2,3,'data',3.14]

print(lst[0])

lst.pop() # last value might delete

print(lst)

lst.pop(2)# second value might delete

print(lst)

lst.append(90)
print(lst) #adding in last value

lst.insert(2,200)#inserting in second value

print(lst)
lst.append(200)
lst.remove(200)# deleting 200 value from the lst

print(lst)

