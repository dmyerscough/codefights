#!/usr/bin/env python


def sumOfTwo(a, b, v):
    '''
    You have two integer arrays, a and b, and an integer target value v.
    Determine whether there is a pair of numbers, where one number is taken
    from a and the other from b, that can be added together to get a sum of v.
    Return true if such a pair exists, otherwise return false.

    >>> a = [1, 2, 3]
    >>> b = [10, 20, 30, 40]
    >>> v = 42
    >>> sumOfTwo(a, b, v)
    True

    >>> a = [1, 2, 3]
    >>> b = [10, 20, 30, 40]
    >>> v = 50
    >>> sumOfTwo(a, b, v)
    False

    '''
    s = set(b)

    for i in a:
        if (v - i) in s:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
