import unittest
from data_structures.doubly_linked_list import *


class DoublyLinkedListCase(unittest.TestCase):
    def _check_linked_list_params(self, test_list, head_value, tail_value, length):
        self.assertEqual(head_value, test_list.head.value)
        self.assertEqual(tail_value, test_list.tail.value)
        self.assertEqual(length, test_list.length)

    def _check_linked_list_empty_params(self, test_list):
        self.assertIsNone(test_list.head)
        self.assertIsNone(test_list.tail)
        self.assertEqual(0, test_list.length)

    def test_empty_linked_list(self):
        test_list = DoublyLinkedList()
        self._check_linked_list_empty_params(test_list)

    def test_append_first(self):
        test_list = DoublyLinkedList()
        test_list.append(10)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=10,
            tail_value=10,
            length=1
        )

    def test_append_multiple(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=9,
            length=10
        )

    def test_get_value_at_index(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        self.assertEqual(3, test_list.get_value_at_index(3))
        self.assertEqual(8, test_list.get_value_at_index(8))

    def test_prepend_first(self):
        test_list = DoublyLinkedList()
        test_list.prepend(10)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=10,
            tail_value=10,
            length=1
        )

    def test_prepend_multiple(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.prepend(i)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=9,
            tail_value=0,
            length=10
        )

    def test_insert_first_correct(self):
        test_list = DoublyLinkedList()
        test_list.insert(10, 0)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=10,
            tail_value=10,
            length=1
        )

    def test_insert_first_oversize(self):
        test_list = DoublyLinkedList()
        test_list.insert(10, 10)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=10,
            tail_value=10,
            length=1
        )

    def test_insert_first_negative(self):
        test_list = DoublyLinkedList()
        test_list.insert(10, -10)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=10,
            tail_value=10,
            length=1
        )

    def test_insert_to_head(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.insert(10, 0)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=10,
            tail_value=9,
            length=11
        )

    def test_insert_to_tail(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.insert(10, 10)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=10,
            length=11
        )

    def test_insert_in_the_middle(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.insert(10, 5)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=9,
            length=11
        )
        self.assertEqual(10, test_list.get_value_at_index(5))

    def test_remove_from_empty(self):
        test_list = DoublyLinkedList()
        self._check_linked_list_empty_params(test_list)
        test_list.remove(0)
        self._check_linked_list_empty_params(test_list)

    def test_remove_oversize(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.remove(10)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=9,
            length=10
        )

    def test_remove_negative(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.remove(-1)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=9,
            length=10
        )

    def test_remove_from_head(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.remove(0)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=1,
            tail_value=9,
            length=9
        )

    def test_remove_from_tail(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.remove(9)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=8,
            length=9
        )

    def test_remove_from_the_middle(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)
        test_list.remove(5)
        self._check_linked_list_params(
            test_list=test_list,
            head_value=0,
            tail_value=9,
            length=9
        )
        self.assertNotEqual(5, test_list.get_value_at_index(5))

    def test_iteration_init(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)

        test_iterator = DoublyLinkedListIterator(test_list)
        self.assertEqual(0, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.head.value)

    def test_iteration_process(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)

        test_iterator = DoublyLinkedListIterator(test_list)
        test_iterator.next()
        test_iterator.next()
        test_iterator.next()
        test_iterator.next()
        test_iterator.next()
        self.assertEqual(5, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.get_value_at_index(5))

        node_1 = test_iterator.previous()
        node_2 = test_iterator.previous()
        self.assertEqual(3, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.get_value_at_index(3))
        self.assertEqual(5, node_1.value)
        self.assertEqual(4, node_2.value)

    def test_iteration_process_edges(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)

        test_iterator = DoublyLinkedListIterator(test_list)

        while True:
            if test_iterator.next() is None:
                break
        self.assertEqual(9, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.tail.value)

        while True:
            if test_iterator.previous() is None:
                break
        self.assertEqual(0, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.head.value)

    def test_iteration_rewind(self):
        test_list = DoublyLinkedList()
        for i in range(0, 10):
            test_list.append(i)

        test_iterator = DoublyLinkedListIterator(test_list)

        test_iterator.next()
        test_iterator.next()
        test_iterator.next()

        test_iterator.rewind()
        self.assertTrue(test_iterator.is_start)
        self.assertFalse(test_iterator.is_finish)
        self.assertEqual(0, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.head.value)

        test_iterator.wind_forward()
        self.assertTrue(test_iterator.is_finish)
        self.assertFalse(test_iterator.is_start)
        self.assertEqual(9, test_iterator.current().value)
        self.assertEqual(test_iterator.pointer.value, test_list.tail.value)


if __name__ == '__main__':
    unittest.main()
