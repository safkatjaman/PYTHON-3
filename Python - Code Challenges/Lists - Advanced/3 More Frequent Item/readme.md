3. More Frequent Item
Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

Define the function to accept three parameters: the list, the first item, and the second item
Count the number of times item1 shows up in our list
Count the number of times item2 shows up in our list
If item1 shows up more, return item1. Otherwise, return item2
Code Challenge
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.