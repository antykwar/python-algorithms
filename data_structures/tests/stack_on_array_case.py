import unittest
from data_structures.stack_on_array import *


class StackOnLinkedListCase(unittest.TestCase):
    def test_push_and_pop(self):
        test_stack = StackOnArray()

        for value in range(10):
            test_stack.push(value)

        stacked_values = []
        while True:
            value = test_stack.pop()
            if value is None:
                break
            stacked_values.append(value)

        expected_values = list(reversed(range(10)))
        self.assertListEqual(expected_values, stacked_values)

    def test_pick_empty(self):
        test_stack = StackOnArray()
        self.assertIsNone(test_stack.pick())

    def test_pick_not_empty(self):
        test_stack = StackOnArray()
        test_stack.push('test')
        self.assertEqual('test', test_stack.pick())

    def test_get_length(self):
        test_stack = StackOnArray()
        self.assertEqual(0, test_stack.get_length())

        for value in range(10):
            test_stack.push(value)
        self.assertEqual(10, test_stack.get_length())

        for i in range(5):
            test_stack.pop()
        self.assertEqual(5, test_stack.get_length())


if __name__ == '__main__':
    unittest.main()
