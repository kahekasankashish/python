'''Take a list of numbers and return a new list which will contain only the distinct elements of the first 
list.'''
def distinct(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    return a
print("New list with distinct elements:",distinct([2,1,5,2,7,5,1,2,3]))
