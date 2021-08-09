def larger_list(lst1, lst2):
      length_1 = len(lst1)
      length_2 = len(lst2)

      if length_1 >= length_2:
            return lst1[-1]
      else:
            return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))