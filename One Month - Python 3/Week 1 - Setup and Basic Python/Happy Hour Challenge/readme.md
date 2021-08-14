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
random_person = random.choice(people)

print(f"How about you go to {random_bar} with {random_person}")
---
---
Happy Hour Challenges
      1. I misspelled Samuel L Jackson's name. Fix the typo.
      2. Add another person to the list of people.
      3. Change the script so it prints out two random people instead of one. (ex. How about you go to Lion's Head Tavern with Mattan and Chris?)