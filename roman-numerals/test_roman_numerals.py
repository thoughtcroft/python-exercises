#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Roman Numerals unit tests"""

import unittest
from ddt import ddt, data, unpack
from roman_numerals import (numeral, round_to_ten,
                            minuend, normalize, convert)

@ddt
class RomanNumeralsTestCase(unittest.TestCase):
    """Unit tests for Roman Numeral function"""

    @data((1, "I"), (50, "L"), (1000, "M"))
    @unpack
    def test_dictionary_numerals(self, first, second):
        """Does the dictionary produce roman numerals?"""
        self.assertEqual(numeral(first), second)
        with self.assertRaises(KeyError):
            numeral(27)

    @data((0, 1), (4, 10), (10, 10), (78, 100), (567, 1000))
    @unpack
    def test_powers_of_ten(self, first, second):
        """Test that we can calculate the next power of 10"""
        self.assertEqual(round_to_ten(first), second)

    @data([(1, 1), (1, 5)], [(1, 50), (1, 100)])
    @unpack
    def test_minuend_returns_factor(self, first, second):
        """Test that minuend is based on next largest factor"""
        self.assertEqual(minuend(first), second)

    @data({'first': [(1, 50), (4, 10), (1, 5), (4, 1)],
           'second': [(1, 10), (1, 100), (1, 1), (1, 10)]})
    @unpack
    def test_normalise_expression(self, first, second):
        """Turn an invalid expression into a valid one"""
        self.assertEqual(normalize(first), second)

    @data((1, "I"), (4, "IV"), (10, "X"), (7, "VII"),
          (99, "XCIX"), (109, "CIX"), (700, "DCC"),
          (999, "CMXCIX"), (1981, "MCMLXXXI"))
    @unpack
    def test_convert_number(self, first, second):
        """Do numbers get correctly turned into roman numerals?"""
        self.assertEqual(convert(first), second)


if __name__ == '__main__':
    unittest.main()
