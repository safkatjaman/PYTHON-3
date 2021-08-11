def larger_sum(lst1, lst2):
      list_sum_1 = 0
      for number in lst1:
            list_sum_1 += number
      
      list_sum_2 = 0
      for number in lst2:
            list_sum_2 += number
      
      if list_sum_1 >= list_sum_2:
            return lst1
      else:
            return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))