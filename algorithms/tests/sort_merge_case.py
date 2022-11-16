import unittest
from algorithms.sort_merge import *


class SortMergeCase(unittest.TestCase):
    def test_sort_merge_correct_work(self):
        self.assertEqual(
            [],
            merge_sort([])
        )
        self.assertEqual(
            [-1, 0, 1, 2, 8, 11, 11, 12, 17, 22, 44, 82],
            merge_sort([2, 8, 1, 17, -1, 11, 44, 22, 11, 0, 82, 12])
        )

    def test_sort_merge_different_types(self):
        with self.assertRaises(TypeError):
            merge_sort([1, None])
