# generally it's a try-except block with finally, else can also be added

try:
    name = str(input('Enter your name: '))
    if(name.isnumeric()):
        raise ValueError('ValueError 😂')
    elif len(name) == 0:
        raise Exception('Empty String! 😂')

# Multiple except blocks are allowed
# except ValueError as ex:
#     print(f'The exception is "{ex}"')

# Better way to handle is to Check the parent "Exception" class **
# Only one except block all cover all exceptions
except Exception as ex:
    print(f'The Exception is "{ex}"')
else:
    name = 'Mr. '+name
    print(f'Else Block: Your name is "{name}"')
finally:
    print('Finally block!')
