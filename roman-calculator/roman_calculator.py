#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Roman Calculator

Perform simple addition of Roman Numerals"""

# python2 and python3 portability
from __future__ import print_function
from builtins import input
from itertools import groupby
from roman_numerals import power_of_ten, ROMAN_NUMERALS

DECIMALS = dict([(v, k) for k, v in ROMAN_NUMERALS.iteritems()])

def decimal(numeral):
    """Returns the number corresponding to the Roman Numeral"""
    return DECIMALS[numeral]

def parse_numerals(numerals):
    """Returns an expression representing Roman Numeral text"""
    return list((sum(1 for _ in y), x) for x, y in groupby(numerals, decimal))

def validate(numerals):
    """Check if the Roman Numeral expression is valid"""
    try:
        expression = parse_numerals(numerals)
    except KeyError:
        # must only contain valid numerals
        return False
    if list(x for x, _ in expression if x > 3):
        # no more than 3 of the same consecutive numerals
        return False
    if len(expression) == 1:
        return True
    prev = expression[0]
    for nxt in expression[1:]:
        if (less_than(prev, nxt) and not
                (power_of_ten(prev) and
                 single_term(prev) and
                 less_than_ten_times(nxt, prev))):
            return False
        prev = nxt
    return True

def convert_to_decimal(numerals):
    """Convert Roman Numerals to decimal equivalent"""
    #assert validate(numerals)
    prev = None
    total = 0
    for term in parse_numerals(numerals):
        if less_than(prev, term):
            total -= term_value(prev) * 2
        total += term_value(term)
        prev = term
    return total

def less_than_ten_times(first, second):
    """Test if terms obey ten times rule"""
    return less_than(first, second, multiple=10)

def single_term(term):
    """Test if a term has a single factor"""
    count, _ = term
    return count == 1

def less_than(first, second, multiple=1):
    """Test if an element is less than another one"""
    if first is None:
        return False
    _, f_factor = first
    _, s_factor = second
    return f_factor <= s_factor * multiple

def term_value(term):
    """Return value of expression term"""
    count, factor = term
    return count * factor

def main():
    """Ask user for the Roman Numeral expression and evaluate it"""
    print()
    expression = input("Enter the Roman Numeral equation to evaluate: ")

    answer = "TBA"
    print()
    print("{} = {}".format(expression, answer))
    print()


if __name__ == '__main__':
    main()
