#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Roman Calculator

Perform simple addition of Roman Numerals"""

# python2 and python3 portability
from __future__ import print_function
from builtins import input

from itertools import groupby
from roman_numerals import (convert_to_numerals,
                            power_of_ten,
                            ROMAN_NUMERALS)

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
    prev = None
    for nxt in expression:
        count, _ = nxt
        if (count > 3 or (count == 2 and not
                          power_of_ten(nxt))):
            return False

        # test the subtraction rules
        if (less_than(prev, nxt) and not
                (power_of_ten(prev) and
                 single_term(prev) and
                 less_than_ten_times(nxt, prev))):
            return False
        prev = nxt
    return True

def convert_to_decimal(numerals):
    """Convert Roman Numerals to decimal equivalent"""
    assert validate(numerals)
    prev = None
    total = 0
    for term in parse_numerals(numerals):
        if less_than(prev, term):
            total -= term_value(prev) * 2
        total += term_value(term)
        prev = term
    return total

def single_term(term):
    """Test if a term has a single factor"""
    count, _ = term
    return count == 1

def less_than_ten_times(first, second):
    """Test if terms obey ten times rule"""
    return less_than(first, second, multiple=10)

def less_than(first, second, multiple=1):
    """Test if an element is less than another one"""
    if not first is None:
        _, f_factor = first
        _, s_factor = second
        return f_factor <= s_factor * multiple

def term_value(term):
    """Return value of expression term"""
    count, factor = term
    return count * factor

def parse_input(equation):
    """Return an equation broken down into terms"""
    return list(x.strip() for x in equation.split('+'))

def main():
    """Ask user for the Roman Numeral expression and evaluate it"""
    print()
    equation = input("Enter the Roman Numeral equation to evaluate: ")
    terms = parse_input(equation)
    if len(terms) < 2:
        print()
        print("Currently you can only add terms!")
        exit()

    # check them for correctness
    errors = list(x for x in terms if not validate(x))
    if errors:
        print()
        for term in errors:
            print("{} is not valid".format(term))
        print()
        exit()

    # compute the sum
    numbers = map(convert_to_decimal, terms)
    total = reduce(lambda x, y: x + y, numbers)
    if total >= 4000:
        print()
        print("-> the result of {} is more than 4000!".format(total))
        print()
        exit()

    # and convert back to Roman Numerals
    result = convert_to_numerals(total)
    print()
    print("-> {} = {}".format(equation, result))
    print()


if __name__ == '__main__':
    main()
