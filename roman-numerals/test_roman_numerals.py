#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from roman_numerals import *


class RomanNumeralsTestCase(unittest.TestCase):
    """Unit tests for Roman Numeral function"""

    def test_dictionary_produces_numerals(self):
        """Does the dictionary produce roman numerals?"""
        for x, y in [(1, "I"), (50, "L"), (1000, "M")]:
            self.assertEqual(numeral(x), y)
        with self.assertRaises(KeyError):
            numeral(27)

    def test_factorize_splits_into_key_chunks(self):
        """Test that a number can be split into key numerals"""
        for x, y in [
            (4, [(4, 1)]),
            (100, [(1, 100)]),
            (357, [(3, 100), (1, 50), (1, 5), (2, 1)]),
            (1981, [(1, 1000), (1, 500), (4, 100), (1, 50), (3, 10), (1, 1)])
        ]:
            self.assertEqual(factorize(x), y)

    def test_find_previous_power_of_ten(self):
        """Test that we can calculate the next power of 10"""
        for x, y in [
            (0, 1), (4, 10), (10, 10), (78, 100), (567, 1000)
        ]:
            self.assertEqual(round_to_ten(x), y)

    def test_minuend_returns_next_biggest_factor(self):
        """Test that minuend is based on next largest factor"""
        for x, y in [
            [(1, 1), (1, 5)]
        ]:
            self.assertEqual(minuend(x), y)

    def test_normalise_expression(self):
        """Turn an invalid expression into a valid one"""
        for x, y in [
            ([(1, 50), (4, 10), (1, 5), (4, 1)], [(1, 10), (1, 100), (1, 1), (1, 10)])
        ]:
            self.assertEqual(normalise(x), y)

    def test_convert_number_to_roman_numerals(self):
        """Do numbers get correctly turned into roman numerals?"""
        for x, y in [
            (1, "I"), (4, "IV"), (10, "X"), (7, "VII"),
            (99, "XCIX"), (109, "CIX"), (700, "DCC"),
            (999, "CMXCIX"), (1981, "MCMLXXXI")
        ]:
            self.assertEqual(convert(x), y)





if __name__ == '__main__':
    unittest.main()
