def odd_indices(lst):
      new_list = []
      for index in range(1, len(lst), 2):
            new_list.append(lst[index])
      return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))