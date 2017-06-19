#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Factorize Unit Tests"""

import unittest
from ddt import ddt, data, unpack
from factorize import factorize, _max_factor, _num_factor, _remainder

FACTORS = list(10**n for n in (9, 6, 3, 2, 1, 0))

@ddt
class FactorizeTestCase(unittest.TestCase):
    """Unit tests for Factorize function"""

    @data((32000, 1000), (1500, 1000), (25, 10), (17, 10), (3, 1))
    @unpack
    def test_largest_lookup_factor(self, first, second):
        """Detects the largest lookup factor in a number"""
        self.assertEqual(_max_factor(first, FACTORS), second)


    @data((132000, 100000, 1), (6400, 1000, 6), (250, 100, 2))
    @unpack
    def test_num_factors(self, first, second, third):
        """Calculates the number of factors in a number"""
        self.assertEqual(_num_factor(first, second), third)

    @data((132000, 100000, 32000), (6400, 1000, 400), (250, 100, 50))
    @unpack
    def test_remainders(self, first, second, third):
        """Calculates the remainder after removing factors"""
        self.assertEqual(_remainder(first, second), third)

    @data((32123, [(32, 1000), (1, 100), (2, 10), (3, 1)]),
          (27, [(2, 10), (7, 1)]),
          (157001, [(157, 1000), (1, 1)]))
    @unpack
    def test_factorize(self, first, second):
        """Test that a number can be broken up into key factors"""
        self.assertEqual(factorize(first, FACTORS), second)


if __name__ == '__main__':
    unittest.main()
