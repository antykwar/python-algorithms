import unittest
from data_structures.queue_on_linked_list import *


class QueueOnLinkedListCase(unittest.TestCase):
    def test_queue_and_dequeue(self):
        test_queue = QueueOnLinkedList()

        for value in range(10):
            test_queue.enqueue(value)

        enqueued_values = []
        while True:
            value = test_queue.dequeue()
            if value is None:
                break
            enqueued_values.append(value)

        expected_values = list(range(10))
        self.assertListEqual(expected_values, enqueued_values)

    def test_pick_empty(self):
        test_queue = QueueOnLinkedList()
        self.assertIsNone(test_queue.pick())

    def test_pick_not_empty(self):
        test_queue = QueueOnLinkedList()
        test_queue.enqueue('test')
        self.assertEqual('test', test_queue.pick())

    def test_get_length(self):
        test_queue = QueueOnLinkedList()
        self.assertEqual(0, test_queue.get_length())

        for value in range(10):
            test_queue.enqueue(value)
        self.assertEqual(10, test_queue.get_length())

        for i in range(5):
            test_queue.dequeue()
        self.assertEqual(5, test_queue.get_length())


if __name__ == '__main__':
    unittest.main()
