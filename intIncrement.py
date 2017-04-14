#!/usr/bin/env python

'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
'''

def increment(arr, pos=-1):
    '''
    >>> c = [1, 2, 3, 4]
    >>> increment(c)
    [1, 2, 3, 5]

    >>> c = [1, 2, 9, 9]
    >>> increment(c)
    [1, 3, 0, 0]

    >>> c = [1, 9, 9]
    >>> increment(c)
    [2, 0, 0]

    '''
    if arr[pos] + 1 > 9:
        arr[pos] = 0
        return increment(arr, pos - 1)
    else:
        arr[pos] += 1

    return arr

if __name__ == '__main__':
    import doctest
    doctest.testmod()
