# Your code below:
single_digits = range(0, 10)
squares = []

for digit in single_digits:
      print(digit)
      squares.append(digit * digit)

print(squares)

cubes = [digit * digit * digit for digit in single_digits]
print(cubes)