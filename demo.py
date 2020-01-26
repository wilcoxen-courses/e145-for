#! /bin/python3
#  Jan 20 (PJW)

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

#  Building the cubes via a list comprehension. This computes
#  all the cubes at oncethe same thing in a more compact (and i
#  often clearer) way.

cubes = [n**3 for n in a_list]

print("\nCubes via list comprehension",cubes)

#  Using range to build lists. A call like range(a,b) call produces 
#  a sequence that starts with 'a' and ends just before 'b'. In the 
#  example below, b_list will start at 1 and end at 5, just like
#  a_list.

b_list = range(1,6)
b_cubes = [b**3 for b in b_list]

print("\nCubes via the range() call")
print("b_cubes:",b_cubes)

