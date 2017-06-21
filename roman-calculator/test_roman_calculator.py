#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-builtin

"""Roman Calculator unit tests"""

import unittest
from ddt import ddt, data, unpack
from roman_calculator import (decimal, validate, parse_numerals,
                              term_value, less_than, less_than_ten_times,
                              parse_input, convert_to_decimal)

@ddt
class RomanCalculatorTestCase(unittest.TestCase):
    """Unit tests for Roman Calculator function"""

    @data(("I", 1), ("L", 50), ("M", 1000))
    @unpack
    def test_dictionary_numerals(self, first, second):
        """Does the dictionary produce roman numerals?"""
        self.assertEqual(decimal(first), second)
        with self.assertRaises(KeyError):
            decimal("Z")

    @data("I", "IV", "XXX", "XCIX", "DCC")
    def test_validate_good_text(self, value):
        """Are correct Roman Numeral texts recognised?"""
        self.assertTrue(validate(value))

    @data("IIII", "IC", "MZM", "XMIX", "VC", "IIV")
    def test_invalidate_bad_text(self, value):
        """Are incorrect Roman Numeral texts recognised?"""
        self.assertIsNotNone(validate(value))
        self.assertFalse(validate(value))

    @data(("III", [(3, 1)]), ("XV", [(1, 10), (1, 5)]),
          ("MCMLXXXI", [(1, 1000), (1, 100), (1, 1000),
                        (1, 50), (3, 10), (1, 1)]))
    @unpack
    def test_parse_input_numerals(self, first, second):
        """Test that we can parse provided numerals"""
        self.assertEqual(parse_numerals(first), second)

    @data([(1, 3), 3], [(5, 10), 50], [(17, 1000), 17000])
    @unpack
    def test_expression_term_value(self, first, second):
        """Test that an expression term can be evaluated"""
        self.assertEqual(term_value(first), second)

    @data([(1, 3), (1, 1), False], [(1, 1), (1, 10), True])
    @unpack
    def test_less_than_term(self, prev, nxt, result):
        """Test that we can detect element ordering"""
        self.assertEqual(less_than(prev, nxt), result)

    @data([(1, 100), (1, 1), False], [(1, 51), (1, 5), False],
          [(1, 5), (1, 1), True], [(1, 100), (1, 10), True])
    @unpack
    def test_less_than_tenx(self, prev, nxt, result):
        """Test that we can detect subtraction limit"""
        self.assertEqual(less_than_ten_times(prev, nxt), result)

    @data(("III", 3), ("XIV", 14), ("XCIX", 99), ("MCMLXXIII", 1973))
    @unpack
    def test_convert_to_decimal(self, first, second):
        """Test that Roman Numerals convert into decimal"""
        self.assertEqual(convert_to_decimal(first), second)

    @data(("I + IV", ["I", "IV"]), ("VI+  X", ["VI", "X"]),
          ("MCM", ["MCM"]), ("XXX - XX", ["XXX - XX"]))
    @unpack
    def test_parse_input(self, first, second):
        """Test that input is properly split into terms"""
        self.assertEqual(parse_input(first), second)


if __name__ == '__main__':
    unittest.main()
