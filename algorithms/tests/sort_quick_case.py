import unittest
from algorithms.sort_quick import *


class SortQuickCase(unittest.TestCase):
    def test_sort_quick_correct_work(self):
        array = []
        quick_sort([])
        self.assertEqual(
            [],
            array
        )
        array = [2, 8, 1, 17, -1, 11, 44, 22, 11, 0, 82, 12]
        quick_sort(array)
        self.assertEqual(
            [-1, 0, 1, 2, 8, 11, 11, 12, 17, 22, 44, 82],
            array
        )

    def test_sort_quick_different_types(self):
        with self.assertRaises(TypeError):
            quick_sort([1, None])
