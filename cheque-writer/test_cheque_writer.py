#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from cheque_writer import *


class ChequeWriterTestCase(unittest.TestCase):
    """Unit tests for Cheque Writer function"""

    def test_dictionary_produces_words(self):
        """Does the dictionary produce words for numbers?"""
        for x, y in [(1, "one"), (15, "fifteen"), (100, "hundred")]:
            self.assertEqual(word(x), y)
        with self.assertRaises(KeyError):
            word(27)

    def test_largest_lookup_factor(self):
        """Detects the largest lookup factor in a number"""
        for x, y in [(32000, 1000), (1500, 1000), (25, 20), (17, 17), (3, 3)]:
            self.assertEqual(max_factor(x, NUMBER_WORDS), y)

    def test_num_factors(self):
        """Calculates the number of factors in a number"""
        for x, y, z in [(132000, 100000, 1), (6400, 1000, 6), (250, 100, 2)]:
            self.assertEqual(num_factor(x, y), z)

    def test_remainders(self):
        """Calculates the remainder after removing factors"""
        for x, y, z in [(132000, 100000, 32000), (6400, 1000, 400), (250, 100, 50)]:
            self.assertEqual(remainder(x, y), z)

    def test_factorize_by_major_factors(self):
        """Test that a number can be broken up into key powers of 10"""
        for x, y in [
                (32123, [(32, 1000), (1, 100), (23, 1)]),
                (27, [(27, 1)]),
                (157001, [(157, 1000), (1, 1)])
        ]:
            self.assertEqual(major_factors(x), y)

    def test_factorize_by_minor_factors(self):
        """Test that a number can be broken down into word numbers"""
        for x, y in [
                (123, [(1, 100), (1, 20), (1, 3)]),
                (27, [(1, 20), (1, 7)]),
                (2, [(1, 2)])
        ]:
            self.assertEqual(minor_factors(x), y)


    def test_convert_to_words(self):
        """Calculates English version of a small number"""
        for x, y in [
                (900, "nine hundred"),
                (132, "one hundred and thirty two"),
                (64, "sixty four"),
                (8, "eight")
        ]:
            self.assertEqual(convert_to_words(x), y)
        with self.assertRaises(AssertionError):
            convert_to_words(1500)

    def test_write_cheque(self):
        """Convert a number into English"""
        self.assertEqual(write_cheque(1357256.32),
                "one million, three hundred and fifty seven thousand, two hundred and fifty six DOLLARS AND thirty two CENTS")
        self.assertEqual(write_cheque(123000),
                "one hundred and twenty three thousand DOLLARS AND zero CENTS")

    def test_dollars_and_cents(self):
        """Split a number into dollar and cents portions"""
        for x, y, z in [(123, 123, 0), (0.25, 0, 25), (15.99, 15, 99)]:
            d, c = dollars_and_cents(x)
            self.assertEqual(d, y)
            self.assertEqual(c, z)


if __name__ == '__main__':
    unittest.main()
