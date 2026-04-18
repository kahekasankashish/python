''' Use a recursive lambda function to find the factorial of a number.'''
f= lambda n: 1 if n==0 else n*f(n-1)
n=int(input("enter a number: "))
print(f(n))