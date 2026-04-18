'''Print nth term in fibonacci series using function.'''
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a=0
    b=1
    for i in range(n-1):
        a,b=b,a+b #1rst calculates right side completely and then assigns the values.Thus in a+b,old value of a is used
    return a #a points to nth term and b points to (n+1)th term
n=int(input("enter n: "))
print(fib(n))