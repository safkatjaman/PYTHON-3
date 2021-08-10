def double_index(lst, index):
      length = len(lst)
      if index > length:
            return lst
      else:
            number_to_be_doubled = lst[index]
            lst[index] = number_to_be_doubled * 2
            return lst

print(double_index([1, 2, 3, 4], 5))