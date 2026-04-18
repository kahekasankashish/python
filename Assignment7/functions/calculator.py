''' WAP to read 2 numbers and a character (among +, -, *, /) and do the corresponding 
calculation. Define different functions for each calculation.'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=eval(input("enter a: "))
b=eval(input("enter b: "))
op=input("enter +,-,* or /: ")
if op=="+":
    print("sum=",add(a,b))
if op=="-":
    print("Diff=",sub(a,b))
if op=="*":
    print("product=",mul(a,b))
if op=="/":
    print("Quotient=",div(a,b))