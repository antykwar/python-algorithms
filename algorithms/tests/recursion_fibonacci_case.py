import unittest
from algorithms.recursion_fibonacci import *


class RecursionFibonacciCase(unittest.TestCase):
    TEST_SEQUENCE = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
        10946,
    ]

    def test_recursive_correct_work(self):
        fibonacci_recursive_fast = fibonacci_recursive_dynamic()
        for i in range(0, len(self.TEST_SEQUENCE)):
            self.assertEqual(self.TEST_SEQUENCE[i], fibonacci_recursive(i))
            self.assertEqual(self.TEST_SEQUENCE[i], fibonacci_recursive_fast(i))

    def test_recursive_correct_work_wrong_arguments(self):
        fibonacci_recursive_fast = fibonacci_recursive_dynamic()
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive_fast(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive(17.3)
        with self.assertRaises(ValueError):
            fibonacci_recursive_fast(17.3)

    def test_recursive_stack_overflow(self):
        fibonacci_recursive_fast = fibonacci_recursive_dynamic()
        with self.assertRaises(RecursionError):
            fibonacci_recursive(2 ** 32)
        with self.assertRaises(RecursionError):
            fibonacci_recursive_fast(2 ** 32)
