4. Odd Indices
This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

Define the function header to accept one input which will be our list of numbers
Create a new list which will hold our values to return
Iterate through every odd index until the end of the list
Within the loop, get the element at the current odd index and append it to our new list
Return the list of elements which we got from the odd indices.
Code Challenge
Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].