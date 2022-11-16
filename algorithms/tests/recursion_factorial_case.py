import unittest
from algorithms.recursion_factorial import *


class RecursionFactorialCase(unittest.TestCase):
    def test_recursive_correct_work(self):
        self.assertEqual(1, factorial_recursive(0))
        self.assertEqual(1, factorial_recursive(1))
        self.assertEqual(120, factorial_recursive(5))
        self.assertEqual(355687428096000, factorial_recursive(17))
        self.assertEqual(10333147966386144929666651337523200000000, factorial_recursive(35))

    def test_recursive_correct_work_wrong_arguments(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(17.3)

    def test_recursive_stack_overflow(self):
        with self.assertRaises(RecursionError):
            factorial_recursive(2 ** 32)
