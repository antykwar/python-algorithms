class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = BinaryTreeNode(value)
        if self.root is None:
            self.root = new_node
            return self
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return self
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return self
                current_node = current_node.right

    def lookup(self, value):
        if self.root is None:
            return None
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node

            if value < current_node.value:
                current_node = current_node.left
                continue
            else:
                current_node = current_node.right
                continue
        return None

    def remove(self, value):
        if self.root is None:
            return None
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if value == current_node.value:
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                        return
                elif current_node.right.left is None:
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        current_node.right.left = current_node.left
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                        return
                else:
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right
                    if parent_node is None:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right

    def breadth_first_search(self):
        if self.root is None:
            return
        current_node = self.root
        values_list = []
        queue_for_children_nodes = [current_node]
        while len(queue_for_children_nodes) > 0:
            current_node = queue_for_children_nodes.pop(0)
            values_list.append(current_node.value)
            if current_node.left is not None:
                queue_for_children_nodes.append(current_node.left)
            if current_node.right is not None:
                queue_for_children_nodes.append(current_node.right)
        return values_list

    def breadth_first_search_recursive(self):
        if self.root is None:
            return []
        return self._traverse_breadth_recursive([self.root], [])

    def _traverse_breadth_recursive(self, queue, values):
        if len(queue) == 0:
            return values
        current_node = queue.pop(0)
        values.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
        return self._traverse_breadth_recursive(queue, values)

    def depth_first_search_in_order(self):
        if self.root is None:
            return []
        return self._traverse_in_order(self.root, [])

    def _traverse_in_order(self, node, values):
        if node.left is not None:
            self._traverse_in_order(node.left, values)
        values.append(node.value)
        if node.right is not None:
            self._traverse_in_order(node.right, values)
        return values

    def depth_first_search_pre_order(self):
        if self.root is None:
            return []
        return self._traverse_pre_order(self.root, [])

    def _traverse_pre_order(self, node, values):
        values.append(node.value)
        if node.left is not None:
            self._traverse_pre_order(node.left, values)
        if node.right is not None:
            self._traverse_pre_order(node.right, values)
        return values

    def depth_first_search_post_order(self):
        if self.root is None:
            return []
        return self._traverse_post_order(self.root, [])

    def _traverse_post_order(self, node, values):
        if node.left is not None:
            self._traverse_post_order(node.left, values)
        if node.right is not None:
            self._traverse_post_order(node.right, values)
        values.append(node.value)
        return values

    def is_valid_bst(self):
        return self._is_valid_bst_traverse(self.root, None, None)

    def _is_valid_bst_traverse(self, node, min_value, max_value):
        if node is None:
            return True
        if (min_value is not None and node.value < min_value) or (max_value is not None and node.value > max_value):
            return False
        return self._is_valid_bst_traverse(
            node.left,
            None,
            node.value - 1
        ) and self._is_valid_bst_traverse(
            node.right,
            node.value + 1,
            None
        )
