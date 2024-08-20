import operator
from math import factorial

# Defined operators with their precedence
ops = {
    '+': (operator.add,1), 
    '-': (operator.sub,1),
    '*': (operator.mul,2),
    '/': (operator.truediv,2),
    '%': (operator.mod,2),
    '!': (None,3) 
}

def apply(operands, operator):
    if operator == '!':
        b=operands.pop()
        if not b.is_integer() or b<0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        operands.append(factorial(int(b)))
    else:
        b=operands.pop()
        a=operands.pop()
        if operator=='/' and b==0:
            raise ZeroDivisionError("Division by zero.")
        operands.append(ops[operator][0](a, b))

def isoperator(c):
    return c in ops

def precedence(op):
    return ops[op][1]

def checking(expression):
    valids='0123456789.+-*/%!()'
    for i,c in enumerate(expression):
        if c not in valids:
            return False
        if c in '+*/%' and (i==0 or expression[i-1] in '+*/%-('):
            return False
        if c == ')' and (i == 0 or expression[i-1] in '+*/%-('):
            return False
        if c == '(' and (i != 0 and (expression[i-1].isdigit() or expression[i-1] == '.')):
            return False
        if c == '!' and (i == 0 or not expression[i-1].isdigit()):
            return False
    return True

def tokenize(expression):
    tokens = []
    num = ''
    for c in expression:
        if c.isdigit() or c == '.':
            num += c
        else:
            if num:
                tokens.append(num)
                num = ''
            tokens.append(c)
    if num:
        tokens.append(num)
    return tokens

def evaluate(tokens):
    operands = []
    operators = []
    i=0
    while i<len(tokens):
        token=tokens[i]
        if token.replace('.','',1).isdigit():
            operands.append(float(token))
        elif token=='(':
            j=i
            ob = 0
            while i<len(tokens):
                if tokens[i] == '(':
                    ob+=1
                elif tokens[i] == ')':
                    ob-=1
                if ob == 0:
                    break
                i+=1
            if ob != 0:
                raise SyntaxError("Mismatched parentheses.")
            operands.append(evaluate(tokens[j+1:i]))
        elif isoperator(token):
            while (operators and precedence(operators[-1])>=precedence(token) and operators[-1]!='('): 
                apply(operands,operators.pop())
            operators.append(token)
        elif token==')':
            while operators and operators[-1] != '(':
                apply(operands,operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
        i+=1
    while operators:
        apply(operands,operators.pop())
    return operands[0]

def calculate(expression):
    try:
        expression=expression.replace(' ', '')
        if not checking(expression):
            raise SyntaxError("Invalid expression")
        tokens=tokenize(expression)
        i=0
        while i<len(tokens):
            if tokens[i]=='-' and (i==0 or tokens[i-1] in '(*'):
                tokens[i]='0'
                tokens.insert(i+1,'-')
            i+=1
        result=evaluate(tokens)
        return result
    except SyntaxError as e:
        return f"Syntax Error: {e}"
    except ZeroDivisionError as e:
        return f"Math Error: {e}"
    except Exception as e:
        return f"Error: {e}"

print('For inputting negative numbers after operators use brackets')
expression=input("Enter your expression: ").strip()
result=calculate(expression)
print(f"Result: {result}")
