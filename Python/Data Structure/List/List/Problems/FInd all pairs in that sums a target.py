lst=[5,6,0,4,1,3,2]
target=7
pairs=[]

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]+lst[j]==target:
            pairs.append((lst[i],lst[j]))
        

print(pairs)