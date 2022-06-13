# Program for a standard calculator

colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[92m',
    'reset': '\033[0m',
    'strikethrough': '\033[09m',
    'bg-lightgrey': '\033[47m'
}


def show(li, showType=False, color='', indices: list = []):
    counter = 0
    for i in li:
        if showType:
            print('S' if type(i) == type('') else 'I', end='')
        else:
            if color != '' and counter in indices:
                print(colors[color], i, colors['reset'], end='')
            else:
                print(i, end=' ')
        counter += 1
    print()


def createTokens(inputExpr: str):
    tokens = []
    token = ''
    for c in inputExpr:
        if c.isnumeric():
            token += c
        elif c == '+' or c == '-' or c == '*' or c == '/' or c == '(' or c == ')' or c == ' ':
            if token != '':
                tokens.append(int(token))
            if c != ' ':
                tokens.append(c)
            token = ''
        else:
            return ['*****   Invalid expression   *****']
    # formatting 1(2)3 as 1*(2)*3, putting '*' where necessary
    for i in range(1, len(tokens)):
        if i+1 < len(tokens) and type(tokens[i+1]) == type(1) and tokens[i] == ')':
            tokens.insert(i+1, '*')
        elif tokens[i] == '(' and type(tokens[i-1]) == type(1):
            tokens.insert(i, '*')
        elif tokens[i] == '(' and tokens[i-1] == ')':
            tokens.insert(i, '*')
    return tokens


def convertToPostfix(tokens):
    postfix = []
    stack = []
    operatorPriority = {
        '/': 4,
        '*': 4,
        '+': 2,
        '-': 2,
    }
    for i in tokens:
        if type(i) == type(1):
            postfix.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                itCount = len(stack)
                for op in range(0, itCount):
                    if stack[-1] != '(':
                        postfix.append(stack.pop())
                    else:
                        break
                stack.pop()
            elif i == '+' or i == '-' or i == '*' or i == '/':
                if not stack.count and (stack[-1] == '(' or operatorPriority[stack[-1]] < operatorPriority[i]):
                    stack.append(i)
                elif len(stack) != 0 and stack[-1] != '(' and operatorPriority[stack[-1]] > operatorPriority[i]:
                    itCount = len(stack)
                    for op in range(0, itCount):
                        if stack[-1] != '(':
                            postfix.append(stack.pop())
                    stack.append(i)
                else:
                    stack.append(i)
        # input() # debug
        # show(stack) # debug
        # show(postfix) # debug
    return postfix


def evaluatePostfix(postfixTokens):
    if len(postfixTokens) < 3:
        return postfixTokens[0]
    i = 2
    while i and len(postfixTokens) >= 3:
        if type(postfixTokens[i-2]) == type(1) and type(postfixTokens[i-1]) == type(1) and not type(postfixTokens[i]) == type(1):
            show(postfixTokens, False, 'red', [i-1, i-2, i])  # debug
            a = postfixTokens[i-2]
            b = postfixTokens[i-1]
            c = postfixTokens[i]
            result = 0
            if c == '+':
                result = a+b
            elif c == '-':
                result = a-b
            elif c == '*':
                result = a*b
            elif c == '/':
                result = a/b
            postfixTokens[i-2] = result
            postfixTokens.pop(i-1)
            postfixTokens.pop(i-1)
            show(postfixTokens, False, 'green', [i-2])  # debug
            print()
            i = 2
        else:
            i += 1
    return postfixTokens[0]

# main function


while(True):
    print(colors['green'], 'Have fun doing math. (, ), *, /, +, - supported!',
          colors['red'], '\nEnter x to quit\n', colors['reset'])
    inputExpression = input()
    # inputExpression = ' 2(1-3)2'  # debug
    inputExpression = '('+inputExpression+')'
    if inputExpression.lower() == '(x)':
        break

    tokens = createTokens(inputExpression)
    print('\nFormatted for evaluation:')
    show(tokens)

    print('Converted to postfix equation:')
    try:
        postfixTokens = convertToPostfix(tokens)
        show(postfixTokens)
        if len(postfixTokens) < 1:
            raise ValueError('*****   Empty expression   *****')
        print('Calculating the result--')
        result = evaluatePostfix(postfixTokens)
    except ValueError as ex:
        print(ex)
    except Exception:
        print('*****   Invalid syntax   *****')
    else:
        print(result)
print('Thanks for using my program 😍')
