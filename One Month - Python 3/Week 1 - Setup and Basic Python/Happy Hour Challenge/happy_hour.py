import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samule L. Jackson"]

random_bar = random.choice(bars)

# 1. I misspelled Samuel L Jackson's name. Fix the typo.
people[-1] = 'Samuel L Jackson'

# 2. Add another person to the list of people.
people.append('Safkat Jaman')
print(people)

# Change the script so it prints out two random people instead of one.
random_person_one = random.choice(people)
random_person_two = random.choice(people)

print(f"How about you go to {random_bar} with {random_person_one} and {random_person_two}")