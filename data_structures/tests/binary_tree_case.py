import unittest
import copy
from data_structures.binary_tree import *


# Test tree:
#     9
#    /  \
#   4   20
#  / \  / \
# 1  6 15 99


class BinaryTreeCase(unittest.TestCase):
    @staticmethod
    def _get_tree_values():
        return [9, 4, 20, 1, 6, 15, 99]

    @staticmethod
    def _get_tree_values_pre_order():
        return [9, 4, 1, 6, 20, 15, 99]

    @staticmethod
    def _get_tree_values_post_order():
        return [1, 6, 4, 15, 99, 20, 9]

    @staticmethod
    def _get_tree_listings_after_remove():
        return {
            None:   [9, 4, 1, 6, 20, 15, 99],
            9:      [15, 4, 1, 6, 20, 99],
            4:      [9, 6, 1, 20, 15, 99],
            20:     [9, 4, 1, 6, 99, 15],
            1:      [9, 4, 6, 20, 15, 99],
            6:      [9, 4, 1, 20, 15, 99],
            15:     [9, 4, 1, 6, 20, 99],
            99:     [9, 4, 1, 6, 20, 15],
        }

    @staticmethod
    def _get_missing_values():
        return [112, 5, 88]

    def test_tree_insert_and_lookup(self):
        tree = BinaryTree()
        for i in self._get_tree_values():
            tree.insert(i)
        self.assertListEqual(self._get_tree_listings_after_remove()[None], tree.depth_first_search_pre_order())
        for i in self._get_tree_values():
            self.assertIsNotNone(tree.lookup(i), f'Could not find {i} in tree')
        for i in self._get_missing_values():
            self.assertIsNone(tree.lookup(i), f'Wrong result for missing value {i} in tree')

    def test_tree_remove_item(self):
        basic_tree = BinaryTree()
        for i in self._get_tree_values():
            basic_tree.insert(i)

        for i in self._get_tree_values():
            tree = copy.deepcopy(basic_tree)
            self.assertIsNotNone(tree.lookup(i))
            tree.remove(i)
            self.assertIsNone(tree.lookup(i), f'Unexpected node {i} - should be removed but exists')
            self.assertListEqual(self._get_tree_listings_after_remove()[i], tree.depth_first_search_pre_order())

    def test_tree_breadth_search(self):
        tree = BinaryTree()
        for i in self._get_tree_values():
            tree.insert(i)
        self.assertListEqual(self._get_tree_values(), tree.breadth_first_search())

    def test_tree_breadth_search_recursive(self):
        tree = BinaryTree()
        for i in self._get_tree_values():
            tree.insert(i)
        self.assertListEqual(self._get_tree_values(), tree.breadth_first_search_recursive())

    def test_tree_depth_first_search_in_order(self):
        tree = BinaryTree()
        for i in self._get_tree_values():
            tree.insert(i)
        in_order_list = self._get_tree_values()
        in_order_list.sort()
        self.assertListEqual(in_order_list, tree.depth_first_search_in_order())

    def test_tree_depth_first_search_pre_order(self):
        tree = BinaryTree()
        for i in self._get_tree_values():
            tree.insert(i)
        self.assertListEqual(self._get_tree_values_pre_order(), tree.depth_first_search_pre_order())

    def test_tree_depth_first_search_post_order(self):
        tree = BinaryTree()
        for i in self._get_tree_values():
            tree.insert(i)
        self.assertListEqual(self._get_tree_values_post_order(), tree.depth_first_search_post_order())

    def test_bst_validation(self):
        bst_tree = BinaryTree()
        for i in self._get_tree_values():
            bst_tree.insert(i)
        self.assertTrue(bst_tree.is_valid_bst())

        non_bst_tree = BinaryTree()
        for i in self._get_tree_values():
            non_bst_tree.insert(i)
        non_bst_tree_2 = copy.deepcopy(non_bst_tree)

        non_bst_tree.root.left.value = 56
        self.assertFalse(non_bst_tree.is_valid_bst())

        non_bst_tree_2.root.right.left.value = 300
        self.assertFalse(non_bst_tree_2.is_valid_bst())
