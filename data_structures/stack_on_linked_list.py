from singly_linked_list import *


class StackOnLinkedList:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, value):
        self.stack.prepend(value)

    def pop(self):
        value = self.stack.get_value_at_index(0)
        self.stack.remove(0)
        return value

    def pick(self):
        value = self.stack.get_value_at_index(0)
        return value

    def get_length(self):
        return self.stack.length
