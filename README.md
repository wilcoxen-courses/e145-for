# Exercise: For Loop Basics

### Summary

Practice with some simple for-loops.

### Deliverables

Your finished repository should have one new script, **for.py**, that 
carries out the steps below.

### Instructions

Please write a script called `for.py` that does the following. See `demo.py`
for examples of some of the steps.

1. Creates a variable called `list1` that consists of the first five
odd integers: 1,3,5,7,9.

1. Print `list1`.

1. Create an empty list called `list2`.

1. Add a for-loop that goes through the elements of `list1`, squares
each value, and then appends that to `list2`. To square a variable called
`n` you would use `n**2`.

1. Create a variable `list3` that uses a list comprehension to do the
squaring instead of an explicit for-loop. Then print `list3`. It should be
identical to `list2`.

1. Add a print statement printing "Table of Powers:" as a heading for
what will come next.

1. Create a variable called `bases` that uses the `range()` call to
build a list of the integers from 1 to 10, inclusive.

1. Create a variable called `powers` that uses `range()` to build a
list of the integers from 0 to 4 inclusive.

1. Create a for-loop over `bases` using `b` as the running variable (
the variable name right after `for`).

1. Inside the loop use a list comprehension to build a list called `values`
that is equal to `b**p` for every `p` in `powers`.

1. Still inside the loop, print a line consisting of "base",`b`,"powers:",
`values`.

### Submitting

Once you're happy with everything and have committed all of the changes to
your local repository, please push the changes to GitHub. At that point,
you're done: you have submitted your answer.
