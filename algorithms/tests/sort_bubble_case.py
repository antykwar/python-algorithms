import unittest
from algorithms.sort_bubble import *


class SortBubbleCase(unittest.TestCase):
    def test_sort_bubble_correct_work(self):
        self.assertEqual(
            [],
            bubble_sort([])
        )
        self.assertEqual(
            [-1, 0, 1, 2, 8, 11, 11, 12, 17, 22, 44, 82],
            bubble_sort([2, 8, 1, 17, -1, 11, 44, 22, 11, 0, 82, 12])
        )

    def test_sort_bubble_different_types(self):
        with self.assertRaises(TypeError):
            bubble_sort([1, None])
