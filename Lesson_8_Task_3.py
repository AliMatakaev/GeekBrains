
def type_logger(func):
   def find_type(arg):
      result = func(arg)
      print(f'{arg}: {type(arg)}')
      return result
   return find_type


@type_logger
def calc_cube(x):
   return x ** 3



a = calc_cube(7)
print(a)