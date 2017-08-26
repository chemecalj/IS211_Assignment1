#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 1, part 1."""


def listDivide(numbers, divide=2):
    """Divides items in a list by a given integer and returns the quantity
    of items which are divisible by that integer.

    Args:
        numbers(list): list of integers.
        divide=2 (int): Arg to divide numbers by.

    Returns:
        int: The number of elements divisible by the divisor.

    Examples:
        >>> listDivide([1,3,7,9])
        0

        >>> listDivide([1,1,2,3,5,8,13], 1)
        7
    """
    dividecount = 0
    for item in numbers:
        if item % divide is 0:
            dividecount += 1
    return dividecount


class ListDivideException(Exception):
    """Invalid calculation class."""
    pass


def testListDivide():
    """A function to test ListDivide."""
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException
    elif listDivide([30, 54, 63, 98, 100], 10) != 2:
        raise ListDivideException
    elif listDivide([]) != 0:
        raise ListDivideException
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

if __name__ == "__main__":
    testListDivide()
