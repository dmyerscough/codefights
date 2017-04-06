#!/usr/bin/env python

import itertools


def tripletSum(x, a):
    '''
    You have an array a composed of exactly n elements. Given a number x,
    determine whether or not a contains three elements for which the sum
    is exactly x.

    >>> x = 15
    >>> a = [14, 1, 2, 3, 8, 15, 3]
    >>> tripletSum(x, a)
    False

    >>> x = 8
    >>> a = [1, 1, 2, 5, 3]
    >>> tripletSum(x, a)
    True

    '''
    for i in itertools.combinations(a, 3):
        if sum(i) == x:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
