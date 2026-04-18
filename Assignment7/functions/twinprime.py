'''Print the twin prime numbers between 2 to 100. Example : pairs of prime numbers that have a 
difference of exactly two. (3, 5), (5, 7), (11, 13), (17, 19) etc.'''
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return n
for i in range(2,101):
    if (prime(i) and prime(i+2)):
            print("(",prime(i),",",prime(i+2),")")