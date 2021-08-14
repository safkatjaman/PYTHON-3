import random

to_do = [
      'Why don\'t you eat some fucking',
      'How about some fucking',
      'Eat a pile of fucking',
      'Will you please fucking eat',
      'Eat some GOD damn fucking',
      'Cook up some fucking',
      'You will not make some fucking',
      'Try some fucking',
      'The New England patriots are the GOD damn worst, oh and eat some fucking'
]

foods_to_eat_meat = [
      'Double-Dusted Fried Chicken',
      'Curried Chicken Salad',
      'Grass-Fed Beef Skirt Steak With Artichoke And Asparagus Salad',
      'Buttermilk Roast Chicken',
      'Gnocchi With Lobster',
      'Lemony Chicken With Mustard Sauce',
      'Southern Buttermilk-Fried Chicken',
      'Pork Chops With Caramelized Apples',
      'Lemon-Rosemary Chicken Thighs',
      'Feta-Spiked Turkey Burgers',
      'BLT Ranch Burgers',
      'American All-Beef Meat Loaf',
      'Russian Onion And Pork Kebabs',
      'Chicken Orzo Pilaf',
      'Boiled Virginia Ham'
]

foods_to_eat_vegetable = [
      'Bearnaise Sauce',
      'Herby Rice Pilaf With Pistachios And Almonds',
      'Salsa',
      'Purple Cabbage And Goat Cheese Saute',
      'Three Sisters Chili',
      'Herb Salad With Lemon Vinaigrette',
      'Sweet Potato Enchiladas',
      'Zucchini Parmesan',
      'Epic Pumpkin Pie Pancakes',
      'Oven-Roasted Vegetable And Pesto Pizza'
]

random_to_do = random.choice(to_do)
random_foods_to_eat_meat = random.choice(foods_to_eat_meat)
random_foods_to_eat_vegetable = random.choice(foods_to_eat_vegetable)


user_name = input('Please enter your name: ')
user_input = input('Do you like meat? (y/n): ')


if user_input == 'y':
      print(f"Hello, {user_name}. {random_to_do} {random_foods_to_eat_meat}.")
elif user_input == 'n':
      print(f"Hello, {user_name}. {random_to_do} {random_foods_to_eat_vegetable}.")
else:
      print(f"Hello, {user_name}. You have to enter only y/n. Thank you! Run the program again.")