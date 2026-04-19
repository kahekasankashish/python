''' Find first ten Fibonacci numbers using recursion.'''
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
num=int(input("enter a number: ")) #no. of terms
for i in range(num):
    print(fib(i), end=" ")