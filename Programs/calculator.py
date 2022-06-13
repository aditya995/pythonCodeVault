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
        if c.isnumeric() or c == '.':
            token += c
        elif c == '+' or c == '-' or c == '*' or c == '/' or c == '(' or c == ')' or c == ' ' or c == '^':
            if token != '':
                tokens.append(float(token))
            if c != ' ':
                tokens.append(c)
            token = ''
        else:
            return ['*****   Invalid expression   *****']
    # formatting 1(2)3 as 1*(2)*3, putting '*' where necessary
    for i in range(1, len(tokens)):
        if i+1 < len(tokens) and type(tokens[i+1]) == type(1.0) and tokens[i] == ')':
            tokens.insert(i+1, '*')
        elif tokens[i] == '(' and type(tokens[i-1]) == type(1.0):
            tokens.insert(i, '*')
        elif tokens[i] == '(' and tokens[i-1] == ')':
            tokens.insert(i, '*')
    return tokens


def convertToPostfix(tokens):
    postfix = []
    stack = []
    operatorPriority = {
        '^': 6,
        '/': 4,
        '*': 4,
        '+': 2,
        '-': 2,
    }
    for i in tokens:
        if type(i) == type(1.0):
            postfix.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            itCount = len(stack)
            for op in range(0, itCount):
                if stack[-1] != '(':
                    postfix.append(stack.pop())
                else:
                    break
            stack.pop()
        elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            if not stack.count and stack[-1] != '(' and operatorPriority[stack[-1]] < operatorPriority[i]:
                stack.append(i)
            elif len(stack) != 0 and stack[-1] != '(' and operatorPriority[stack[-1]] > operatorPriority[i]:
                itCount = len(stack)
                for op in range(0, itCount):
                    if stack[-1] != '(':
                        postfix.append(stack.pop())
                    else:
                        break
                stack.append(i)
            elif not stack.count and (stack[-1] != '(' and operatorPriority[stack[-1]] == operatorPriority[i]):
                postfix.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        # input()  # debug
        show(stack)  # debug
        show(postfix)  # debug
    return postfix


def evaluatePostfix(postfixTokens):
    if len(postfixTokens) < 3:
        return postfixTokens[0]
    cStack = []
    for i in postfixTokens:
        if type(i) == type(1.0):
            cStack.append(i)
        else:
            if i == '+':
                result = cStack[-2]+cStack[-1]
            elif i == '-':
                result = cStack[-2]-cStack[-1]
            elif i == '*':
                result = cStack[-2]*cStack[-1]
            elif i == '/':
                result = cStack[-2]/cStack[-1]
            elif i == '^':
                result = cStack[-2]**cStack[-1]
            cStack.pop()
            cStack[-1] = result
    return cStack[0]

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
    except Exception as ex:
        print(ex, '*****   Invalid syntax   *****')
    else:
        print(result, 1*(3-4)*5+5*2*(1+2))
print('Thanks for using my program 😍')
