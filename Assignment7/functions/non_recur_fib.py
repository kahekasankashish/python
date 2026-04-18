''' Find first ten Fibonacci numbers using non-recursive function.'''
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    c=a+b
    while c<=n:
        print(c)
        a=b
        b=c
        c=a+b
n=int(input("enter n:"))
fib(n)
