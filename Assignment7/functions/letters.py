'''Accepts a string and counts the number of upper and lower case letters.'''
def count(str):
    u=0
    l=0
    for s in str:
        if s.isupper():
            u+=1
        if s.islower():
            l+=1
    print("no. of upper case letters=",u,"and no. of lower case letters=",l)
str=input("enter a string: ")
count(str)
