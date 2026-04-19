''' Create a list containing five numbers. Create another list which will contain the cube of the numbers 
of the first list using map().
OR
. Define a one-line procedure cubes(L) specified as follows:  
a. input: list L of numbers  
b. output: list of numbers whose ith element is the cube of the ith element of L  
Example: input [1, 2, 3], output [1,8, 27]. '''

l=eval(input("enter a list elements within []: "))
cube=list(map(lambda x: x**3,l))
print(cube)