4. Double Index
Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
Test if the index is invalid. If its invalid then return the original list
If the list is valid then get all values up to the index and store it as a new list
Append the value at the index times 2 to the new list
Add the rest of the list from the index onto the new list
Return the new list
Code Challenge
Create a function named double_index that has two parameters: a list named lst and a single number named index.

The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.

If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)