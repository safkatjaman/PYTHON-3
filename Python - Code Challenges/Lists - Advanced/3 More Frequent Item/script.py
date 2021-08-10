def more_frequent_item(lst, item1, item2):
      item_1_on_list = lst.count(item1)
      item_2_on_list = lst.count(item2)

      if item_1_on_list >= item_2_on_list:
            return item1
      else:
            return item2

print(more_frequent_item(input('Enter a list of items: '), input('Enter item 1: '), input('Enter item 2: ')))