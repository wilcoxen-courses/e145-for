'''
Demonstrate the use of for loops.
Spring 2022 PJW
'''

#  Create a simple numerical list

a_list = [1,2,3,4,5]

print("\na_list:",a_list)

#  Loop through the list computing the cubes. Collect them in a 
#  new list that starts out empty.

a_cubes = []
for n in a_list:
    a_cubes.append( n**3 )

print("\nInitial list:",a_list)
print("Cubes via for loop:",a_cubes)

#  Build the cubes via a list comprehension. This computes
#  all the cubes at once. It's more compact and often
#  clearer than using a regular for loop.

cubes = [n**3 for n in a_list]

print("\nCubes via list comprehension",cubes)

#  Use range to build the cubes. A call like range(a,b) produces 
#  a sequence that starts with 'a' and ends just before 'b'. In the 
#  example below, b_list will start at 1 and end at 5, just like
#  a_list. As a result, the cubes will be identical.

b_list = range(1,6)
b_cubes = [b**3 for b in b_list]

print("\nCubes via the range() call")
print("b_cubes:",b_cubes)
