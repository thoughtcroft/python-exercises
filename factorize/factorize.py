#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Factorize

Helpers to create expressions of numbers factored into key
amounts for use in numbers to words, Roman Numerals etc"""

FACTORS = list(10**n for n in (9, 6, 3, 2, 0))

def factorize(number, factors, result=None):
    """Divide a number into the supplied factors

    Returns a list of tuples of the form (x, y)
    where x is the count of the y factor
    """
    if result is None:
        result = []
    factor = _max_factor(number, factors)
    amount = _num_factor(number, factor)
    remain = _remainder(number, factor)
    result.append((amount, factor))
    if remain == 0:
        return result
    return factorize(remain, factors, result)

def _max_factor(number, factors):
    """Determines the largest factor present in a number"""
    return max(n for n in factors if n <= number)

def _num_factor(number, factor):
    """Return the number of factors in the number"""
    assert factor != 0
    return number // factor

def _remainder(number, factor):
    """Return the remainder after removing factor"""
    assert factor != 0
    return number % factor
