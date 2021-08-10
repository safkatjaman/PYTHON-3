def middle_element(lst):
      length = len(lst)

      if length % 2 != 0:
            return lst[int(length / 2)]
      else:
            return (lst[int(length / 2)] + lst[int((length / 2) - 1)]) / 2

print(middle_element([5, 2, -10, -4, 4, 5]))