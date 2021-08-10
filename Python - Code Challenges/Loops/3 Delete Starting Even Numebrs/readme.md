3. Delete Starting Even Numbers
Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

Define our function to accept a single input parameter lst which is a list of numbers
Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
Within the loop, if the first number in the list is even, then remove the first number of the list
Once we hit an odd number or we run out of numbers, return the modified list
Code Challenge
Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!