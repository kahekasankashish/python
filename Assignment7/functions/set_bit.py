''' Define a function that will take input as number and return the number of set bit of the given number.'''
def set(n):
    temp=n
    bin=0
    m=1
    while(n>0):
        r=int(n%2)
        bin=bin+r*m
        m=m*10
        n=n//2
    c=0
    while bin>0:
        d=int(bin%10)
        if d==1:
            c+=1
        bin=bin//10
    return c
n=int(input("enter a number: "))
print("No. of set bits=",set(n))


