import re

print('Enter "quit" to exit the calculator.')
run = True 
result = 0

def calculator():
    global run 
    global result
    input_equation = input('Enter equation: ').lower()
    if input_equation == 'quit':
        print("Thanks for using the calculator")
        run = False
    else:
        input_equation = re.sub('[a-zA-Z,:;]', ' ', input_equation)
        result = eval(input_equation)
        print(result)

while run:
    calculator()