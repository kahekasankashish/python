''' Find the reverse of a number using recursion.'''
def rev_num(n,rev=0):
    if n==0:
        return rev
    rev=rev*10+(n%10)
    return rev_num(n//10,rev)
n=int(input("enter a no.: "))
print(rev_num(n,0))