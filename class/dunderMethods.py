# Dunder or magic methods in python:
# 5 DUNDER METHODS TO KNOW -
# Operator Dunder Methods
# __str__
# __len__
# Assignment Dunder Methods
# __getitem__


# Operator Dunder/Magic Methods **

# __sub__ for subtraction(-) 
# __mul__ for multiplication(*)
# __truediv__ for division(/)
# __eq__ for equality (==)
# __lt__ for less than(<)
# __gt__ for greater than(>)
# __le__ for less than or equal to (≤)
# __ge__ for greater than or equal to (≥)

class Account:
  def __init__(self, account_name, balance=0):
    self.account_name = account_name
    self.balance = balance
  def __add__(self,acc):
    if isinstance(acc,Account):
      return self.balance  + acc.balance
    raise Exception(f"{acc} is not of class Account")

# See more here https://builtin.com/data-science/dunder-methods-python