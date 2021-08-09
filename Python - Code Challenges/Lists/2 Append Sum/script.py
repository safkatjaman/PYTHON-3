def append_sum(lst):
      append_1 = lst[-1] + lst[-2]
      lst.append(append_1)

      append_2 = lst[-1] + lst[-2]
      lst.append(append_2)

      append_3 = lst[-1] + lst[-2]
      lst.append(append_3)

      return lst

print(append_sum([1, 1, 2]))