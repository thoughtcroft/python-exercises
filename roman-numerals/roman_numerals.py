#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Roman Numerals

Converts an integer less than 4000
into the equivalent Roman Numerals"""

# python2 and python3 portability
from __future__ import print_function
from builtins import input
from factorize import factorize

ROMAN_NUMERALS = {
    1: "I", 5: "V", 10: "X", 50: "L",
    100: "C", 500: "D", 1000: "M"
    }


def numeral(number):
    """Returns the Roman Numeral for the key number"""
    return ROMAN_NUMERALS[number]

def normalize(expression):
    """Ensure expression satisfies Roman Numeral rules

    if 4 numerals then work out subtract term
    - don't subtract from a number more than 10 x greater
    - only subtract from powers of 10
    """
    if not list(x for x, _ in expression if x == 4):
        return expression
    result = []
    prev = None
    for elem in expression:
        count, factor = elem
        if count == 4:
            if power_of_ten(prev):
                prev = minuend(elem)
            else:
                result.pop()
                prev = minuend(prev)
            result.append((1, factor))
        else:
            prev = elem
        result.append(prev)
    return result

def power_of_ten(term):
    """Is this term describing a power of ten?"""
    if term is None:
        return True
    _, factor = term
    return round_to_ten(factor) == factor

def minuend(term):
    """Return the minuend for the supplied subrahend"""
    keys = sorted(ROMAN_NUMERALS.keys())
    _, factor = term
    next_factor = keys[keys.index(factor) + 1]
    return (1, next_factor)

def round_to_ten(number):
    """Round number up to next power of 10"""
    count = len(str(int(number)))
    if number % 10 == 0:
        count = count - 1
    return 10 ** count

def convert(number):
    """Return the Roman Numerals coresponding to number"""
    assert number < 4000
    number = int(number)
    result = []
    expression = factorize(number, ROMAN_NUMERALS)
    for count, factor in normalize(expression):
        result.append(numeral(factor) * count)
    return "".join(result)


def main():
    """Ask user for the decimal number and print it in Roman Numerals"""
    print()
    number = input("Enter the number to be converted (whole numbers only, < 4000): ")

    if float(number) >= 4000 or float(number) <= 0:
        print("That number is out of range!")
        exit()
    print()
    print("{} is the same as {}".format(number, convert(int(number))))
    print()


if __name__ == '__main__':
    main()
