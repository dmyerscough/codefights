#!/usr/bin/env python

import re

def evaluate(expression):
    '''
    Evaluate the a string into a mathmatic formula

    >>> evaluate('1+1')
    2
    >>> evaluate('1+1*10')
    20
    >>> evaluate('5+5*10*100')
    10000
    '''
    stack = []
    numbers = []
    operators = []

    expression = filter(None, re.split('(\d+)', expression))

    for i in expression:
        if i.isdigit():
            numbers.append(int(i))
        else:
            operators.append(i)

    for i in numbers:
        if stack:
            left, right = int(stack.pop()), int(i)
            operator = operators.pop(0)

            if operator == '+':
                stack.append(left + right)
            elif operator == '*':
                stack.append(left * right)
            elif operator == '/':
                stack.append(left / right)
            elif operator == '-':
                stack.append(left - right)
        else:
            stack.append(int(i))

    return stack.pop()


if __name__ == '__main__':

    import doctest
    doctest.testmod()
