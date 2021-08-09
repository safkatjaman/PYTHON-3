def append_size(lst):
      length = len(lst)
      lst.append(length)
      return lst

print(append_size([10, 20, 30, 40, 50]))