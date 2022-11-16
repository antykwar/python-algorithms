import unittest
from algorithms.recursion_reverse_string import *


class RecursionFibonacciCase(unittest.TestCase):
    TEST_CASES = ['test', 'Some string to test']

    def test_function_results(self):
        for initial_string in self.TEST_CASES:
            self.assertEqual(initial_string[::-1], reverse_string(initial_string))
