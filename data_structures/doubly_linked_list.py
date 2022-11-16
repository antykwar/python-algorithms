from __future__ import annotations


class DoublyLinkedListIterator:
    def __init__(self, linked_list: DoublyLinkedList):
        self.linked_list = linked_list
        self.pointer = self.linked_list.head
        self.is_start = True
        self.is_finish = False

    def current(self):
        return self.pointer

    def next(self):
        if self.is_finish:
            return None
        current_node = self.pointer
        self.is_start = False
        if self.pointer.next_node is not None:
            self.pointer = self.pointer.next_node
        else:
            self.is_finish = True
        return current_node

    def previous(self):
        if self.is_start:
            return None
        current_node = self.pointer
        self.is_finish = False
        if self.pointer.previous_node is not None:
            self.pointer = self.pointer.previous_node
        else:
            self.is_start = True
        return current_node

    def rewind(self):
        self.pointer = self.linked_list.head
        self.is_start = True
        self.is_finish = False

    def wind_forward(self):
        self.pointer = self.linked_list.tail
        self.is_start = False
        self.is_finish = True


class DoublyListNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def _add_first_node(self, node: DoublyListNode):
        self.head = self.tail = node
        self.length += 1

    def _get_node_at_index(self, index: int):
        if index >= self.length or index < 0:
            return None
        counter = 0
        current_node = self.head
        while counter < index:
            current_node = current_node.next_node
            counter += 1
        return current_node

    def get_value_at_index(self, index: int):
        current_node = self._get_node_at_index(index)
        if current_node is not None:
            return current_node.value
        return None

    def append(self, value):
        node = DoublyListNode(value)
        current_tail = self.tail
        if current_tail is None:
            self._add_first_node(node)
            return
        self.tail.next_node = node
        node.previous_node = self.tail
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = DoublyListNode(value)
        current_head = self.head
        if current_head is None:
            self._add_first_node(node)
            return
        node.next_node = current_head
        current_head.previous_node = node
        self.head = node
        self.length += 1

    def insert(self, value, index: int):
        current_node = self.head

        if index <= 0:
            self.prepend(value)
            return

        if index >= self.length:
            self.append(value)
            return

        node = DoublyListNode(value)

        if current_node is None:
            self._add_first_node(node)
            return

        parent_node = self._get_node_at_index(index - 1)

        node.next_node = parent_node.next_node
        parent_node.next_node.previous_node = node

        parent_node.next_node = node
        node.previous_node = parent_node

        self.length += 1
        if index == self.length - 1:
            self.tail = node

    def remove(self, index: int):
        current_node = self.head

        if index >= self.length or index < 0 or current_node is None:
            return

        if index == 0:
            if current_node.next_node is None:
                self.head = self.tail = None
            else:
                self.head = current_node.next_node
                self.head.previous_node = None
            self.length -= 1
            return

        parent_node = self._get_node_at_index(index - 1)
        node_to_remove = parent_node.next_node
        parent_node.next_node = node_to_remove.next_node

        if parent_node.next_node is not None:
            parent_node.next_node.previous_node = parent_node

        if index == self.length - 1:
            self.tail = parent_node
        self.length -= 1
