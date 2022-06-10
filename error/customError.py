class MyCustomError(Exception):
    pass


class NoneVal(MyCustomError):
    # If the value is None
    pass


class EmptyStringVal(MyCustomError):
    # If the value is Empty String
    pass


value = None
try:
    if value == '':
        raise NoneVal('"Value can not be None"')
    if value == '':
        raise EmptyStringVal('"Value can not be Empty String"')
    else:
        print(value)
except Exception as ex:
    print(f'The exception is {ex}')
else:
    print(f'The assignment is done')
