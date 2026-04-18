'''Find the reverse of a string.'''
def rev(str):
    r=""
    for i in range(len(str)-1,-1,-1):
        r=r+str[i]
    return r
str=input("Enter a string: ")
print(rev(str))