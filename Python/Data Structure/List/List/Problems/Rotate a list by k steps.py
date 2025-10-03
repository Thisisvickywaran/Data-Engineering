
lst=[1,2,3,4,5,67,8]
k=-1

k=k%len(lst)
rotated = lst[-k:] + lst[:-k]

print(rotated)