from singly_linked_list import *


class StackOnArray:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.get_length() == 0:
            return None
        return self.stack.pop()

    def pick(self):
        if self.get_length() == 0:
            return None
        return self.stack[-1]

    def get_length(self):
        return len(self.stack)
