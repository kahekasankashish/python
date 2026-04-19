''' Filter the odd numbers present in a list by using filter().'''
l=eval(input("enter a list elements within []: "))
odd=list(filter(lambda x: x%2 ==1,l))
print(odd)