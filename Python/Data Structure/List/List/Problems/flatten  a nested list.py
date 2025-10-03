lst=[[1,2],[3,4],[5,6],[7,[8,9]]]

flat=[]

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flat.append(item)


flatten(lst)
print(flat)
