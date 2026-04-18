''' Find the greatest among three numbers using lambda function. '''
f= lambda a,b,c: a if (a>b and a>c) else (b if b>a and b>c else c)
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
print("Greatest=",f(a,b,c))