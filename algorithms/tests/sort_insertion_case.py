import unittest
from algorithms.sort_insertion import *


class SortInsertionCase(unittest.TestCase):
    def test_sort_insertion_correct_work(self):
        self.assertEqual(
            [],
            insertion_sort([])
        )
        self.assertEqual(
            [-1, 0, 1, 2, 8, 11, 11, 12, 17, 22, 44, 82],
            insertion_sort([2, 8, 1, 17, -1, 11, 44, 22, 11, 0, 82, 12])
        )

    def test_sort_bubble_different_types(self):
        with self.assertRaises(TypeError):
            insertion_sort([1, None])
