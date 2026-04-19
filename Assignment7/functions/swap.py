'''Swap the values between two numbers.
 Use keyword arguments as parameters.  
 '''
def swap(**kwargs):
 a=kwargs.get('a')
 b=kwargs.get('b')
 if a==None or b==None:
  print("Enter two numbers exactly.")
  return
 a,b=b,a
 print("After swapping:",a,b )
swap(a=10,b=20)