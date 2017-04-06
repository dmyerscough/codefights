#!/usr/bin/env python


def stringPermutations(origin_str, s, p=None, c=''):
    '''
    Given a string s, find all its potential permutations.
    The output should be sorted in lexicographical order.

    >>> s = 'CBA'
    >>> stringPermutations(s, s)
    ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

    >>> s = "ABA"
    >>> stringPermutations(s, s)
    ['AAB', 'ABA', 'BAA']

    '''
    if p is None:
        p = []

    if len(c) == len(origin_str):
        p.append(c)
        return

    for i in range(0, len(s)):
        stringPermutations(origin_str, s[0:i] + s[i + 1:], p, c + s[i])

    return sorted(set(p))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
