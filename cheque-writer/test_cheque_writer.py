#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for Cheque Writer module"""


import unittest
from ddt import ddt, data, unpack
from cheque_writer import (convert_to_words, dollars_and_cents,
                           major_factors, minor_factors, word,
                           remove_trailing_terms, write_cheque)

@ddt
class ChequeWriterTestCase(unittest.TestCase):
    """Unit tests for Cheque Writer function"""

    @data((1, "one"), (15, "fifteen"), (100, "hundred"))
    @unpack
    def test_dictionary_produces_words(self, first, second):
        """Does the dictionary produce words for numbers?"""
        self.assertEqual(word(first), second)
        with self.assertRaises(KeyError):
            word(27)

    @data((32123, [(32, 1000), (1, 100), (23, 1)]),
          (27, [(27, 1)]),
          (157001, [(157, 1000), (1, 1)]))
    @unpack
    def test_factorize_by_major_factors(self, first, second):
        """Test that a number can be broken up into key powers of 10"""
        self.assertEqual(major_factors(first), second)

    @data((123, [(1, 100), (1, 20), (1, 3)]),
          (27, [(1, 20), (1, 7)]),
          (2, [(1, 2)]))
    @unpack
    def test_factorize_by_minor_factors(self, first, second):
        """Test that a number can be broken down into word numbers"""
        self.assertEqual(minor_factors(first), second)

    @data((900, "nine hundred"),
          (132, "one hundred and thirty two"),
          (64, "sixty four"),
          (10, "ten"),
          (8, "eight"))
    @unpack
    def test_convert_to_words(self, first, second):
        """Calculates English version of a small number"""
        self.assertEqual(convert_to_words(first), second)
        with self.assertRaises(AssertionError):
            convert_to_words(1500)

    @data((1357256.32, ("one million, three hundred and "
                        "fifty seven thousand, two hundred and "
                        "fifty six DOLLARS AND thirty two CENTS")),
          (123000, ("one hundred and twenty three thousand "
                    "DOLLARS AND zero CENTS")),
          (100.10, "one hundred DOLLARS AND ten CENTS"),
          (1.01, "one DOLLAR AND one CENT"),
          (1200.21, "one thousand, two hundred DOLLARS AND twenty one CENTS"))
    @unpack
    def test_write_cheque(self, first, second):
        """Convert a number into English"""
        self.assertEqual(write_cheque(first), second)

    @data((123, 123, 0), (0.25, 0, 25), (15.99, 15, 99), (1.10, 1, 10))
    @unpack
    def test_dollars_and_cents(self, first, second, third):
        """Split a number into dollar and cents portions"""
        dollars, cents = dollars_and_cents(first)
        self.assertEqual(dollars, second)
        self.assertEqual(cents, third)

    @data((['test', 'no', 'change'], ['test', 'no', 'change']),
          (['test', 'remove', 'and'], ['test', 'remove']),
          (['test', 'comma,'], ['test', 'comma']))
    @unpack
    def test_remove_trailing_terms(self, first, second):
        """It removes trailing 'and' and ',' terms"""
        remove_trailing_terms(first)
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
