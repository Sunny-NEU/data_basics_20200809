#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/12 10:46
#!@Author: Zhang-sl

import unittest
from fib import fib


class FibTest(unittest.TestCase):
    def test_generate_5_fibs(self):
        self.assertEqual(fib(5), [1, 1, 2, 3, 5])

    def test_generate_10_fibs(self):
        self.assertEqual(fib(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_generate_negative_number_fibs(self):
        self.assertEqual(fib(-1), None)

    def test_generate_0_number_fibs(self):
        self.assertEqual(fib(0), None)

    def test_generate_1_number_fibs(self):
        self.assertEqual(fib(1), [1])

    def test_generate_2_number_fibs(self):
        self.assertEqual(fib(2), [1, 1])


if __name__ == '__main__':
    unittest.main()