#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Cheque Writer

Takes a numerical monetary value as input and outputs
its English equivalent so it can be written on a cheque"""

# python2 and python3 portability
from __future__ import print_function
from builtins import input

from factorize import factorize

NUMBER_WORDS = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety", 10**2: "hundred",
    10**3: "thousand,", 10**6: "million,", 10**9: "billion,"
    }

KEY_POWERS_OF_TEN = list(10**n for n in (9, 6, 3, 2, 0))


def major_factors(number):
    """Return the major power-of-ten factors"""
    return factorize(number, KEY_POWERS_OF_TEN)

def minor_factors(number):
    """Return the word number factors"""
    return factorize(number, NUMBER_WORDS)

def word(number):
    """Return word associated with factor"""
    return NUMBER_WORDS[number]

def convert_to_words(number):
    """Return the English version of a small number"""
    assert number < 1000
    if number == 0:
        return word(0)
    result = []
    for count, factor in minor_factors(number):
        if factor == 100:
            result.append(word(count))
            result.append(word(100))
            result.append('and')
        else:
            result.append(word(factor))
    if result[-1] == 'and':
        result.pop(-1)
    return " ".join(result)

def dollars_and_cents(number):
    """Return dollars and cents portions"""
    dollars = int(number)
    cents = int(round((number - dollars) * 100))
    return (dollars, cents)

def write_cheque(number):
    """Return the English equivalent of a cheque number"""
    assert number < 2 * 10**9
    dollars, cents = dollars_and_cents(number)
    result = []

    for count, factor in major_factors(dollars):
        result.append(convert_to_words(count))
        if factor != 1:
            result.append(word(factor))
        if factor == 100:
            result.append('and')

    # remove any trailing comma or and
    if result[-1] == 'and':
        result.pop(-1)
    if result[-1][-1] == ',':
        result[-1] = result[-1][:-1]

    if dollars == 1:
        result.append('DOLLAR AND')
    else:
        result.append('DOLLARS AND')
    result.append(convert_to_words(cents))
    if cents == 1:
        result.append('CENT')
    else:
        result.append('CENTS')
    return " ".join(result)


def main():
    """Ask user for the cheque amount and print it in English"""
    print()
    amount = input("Enter the cheque amount in dollars and cents (numbers only, < 2 billion): ")

    if float(amount) >= 2000000000 or float(amount) <= 0:
        print("That amount is out of range!")
        exit()
    print()
    print("Cheque amount is: {}".format(write_cheque(float(amount))))
    print()


if __name__ == '__main__':
    main()
