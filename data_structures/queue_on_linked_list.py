from singly_linked_list import *


class QueueOnLinkedList:
    def __init__(self):
        self.queue = SinglyLinkedList()

    def pick(self):
        value = self.queue.get_value_at_index(0)
        return value

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        value = self.queue.get_value_at_index(0)
        self.queue.remove(0)
        return value

    def get_length(self):
        return self.queue.length
