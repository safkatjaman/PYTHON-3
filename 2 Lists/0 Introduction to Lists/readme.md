INTRODUCTION TO LISTS

Review

So far, we have learned:

How to create a list
How to access, add, remove, and modify list elements
How to create a two-dimensional list
How to access and modify two-dimensional list elements
Let’s practice these skills.

Instructions
1.
Maria is entering customer data for her web store business. We’re going to help her organize her data.

Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:

Ainsley
Ben
Chani
Depak


2.
Maria wants to track all customer’s preferred sizes for her clothing. Create a list called preferred_size.

Fill our new list preferred_size with the following data, containing the preferred sizes for Ainsley, Ben, and Chani:

["Small", "Large", "Medium"]


3.
On no! We forgot to add Depak’s size.

Depak’s size is "Medium". Use .append() to add "Medium" to the preferred_size list.

Print preferred_size to see our change.


4.
Maria is having a hard time visualizing which customer is associated with each size. Let’s restructure our two lists into a two-dimensional list to help Maria.

In addition to our already available data, Maria is adding a third value for each customer that reflects if they want expedited shipping on their orders.

This will be reflected using a boolean value (True for expedited, False for regular)

Create a two-dimensional list called customer_data using the following table as a reference for the data. Each sublist should contain a name, size, and expedited shipping option for a single person.

Name	Size	Expedited Shipping
"Ainsley"	"Small"	True
"Ben"	"Large"	False
"Chani"	"Medium"	True
"Depak"	"Medium"	False

Print customer_data to see the data.


5.
"Chani" reached out to Maria. She requested to switch to regular shipping to save some money.

Change the data value for "Chani"‘s shipping preference to False in our two-dimensional list to reflect the change.


6.
"Ben" reached out to Maria asking to remove his shipping option because he is not sure what type he wants.

Use the .remove() method to delete the shipping value from the sublist that contains ben’s data.

Note: We never explicitly went over how to use the .remove() method on a 2d list together. If you feel like you are struggling, take a look at the hint for some guidance.


7.
Great job making it this far! One last thing, Maria received a new customer "Amit" and "Karim" that had the following data:

[["Amit", "Large", True], ["Karim", "X-Large", False]]
Create a new variable customer_data_final. Combine our existing list customer_data with our new customer 2d list using + by adding it to the end of customer_data.

Print customer_data_final to see our final result.