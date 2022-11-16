import unittest
from algorithms.sort_selection import *


class SortSelectionCase(unittest.TestCase):
    def test_sort_selection_correct_work(self):
        self.assertEqual(
            [],
            selection_sort([])
        )
        self.assertEqual(
            [-1, 0, 1, 2, 8, 11, 11, 12, 17, 22, 44, 82],
            selection_sort([2, 8, 1, 17, -1, 11, 44, 22, 11, 0, 82, 12])
        )

    def test_sort_selection_different_types(self):
        with self.assertRaises(TypeError):
            selection_sort([1, None])
