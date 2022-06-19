
def val_checker(func):
   def find_val(arg):
      if arg < 0:
         raise ValueError('Wrong val:', arg)
      result = func(arg)
      return result
   return find_val


@val_checker
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
print(a)