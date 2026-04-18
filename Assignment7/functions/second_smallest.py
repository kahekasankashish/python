'''Define a function, which will take one parameter as a list and return the 2nd smallest element of the 
list.'''
def small(l):
    fmin=l[0]
    smin=l[0]
    for i in l:
        if i<fmin:
            fmin=i
    for i in l:
        if i>fmin and i<smin:
            smin=i
    return smin
print(small([5,1,3,8,4,2]))  