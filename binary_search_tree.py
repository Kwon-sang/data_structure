from node import TreeNode
from queue import Queue


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value, node=None):
        if not node:
            node = self.root
        if not self.root:
            return False

        if value == node.value:
            return True
        elif value > node.value:
            if not node.node_RHS:
                return False
            else:
                return self.search(value=value, node=node.node_RHS)
        else:
            if not node.node_LHS:
                return False
            else:
                return self.search(value=value, node=node.node_LHS)

    def insert(self, value, node=None):
        if not node:
            node = self.root
        if not self.root:
            self.root = TreeNode(value=value)
            return

        if value == node.value:
            return
        elif value > node.value:
            if not node.node_RHS:
                node.node_RHS = TreeNode(value=value, node_parent=node)
                return
            else:
                self.insert(value=value, node=node.node_RHS)
        else:
            if not node.node_LHS:
                node.node_LHS = TreeNode(value=value, node_parent=node)
                return
            else:
                self.insert(value=value, node=node.node_LHS)

    def delete(self, value, node=None):
        if not node:
            node = self.root
        if not self.root:
            raise ValueError("The tree is empty")

        if value > node.value:
            return self.delete(value, node.node_RHS)
        if value < node.value:
            return self.delete(value, node.node_LHS)
        if value == node.value:
            # The case of existing Two-Child : hoisting the minimum value of subtree
            if node.node_LHS and node.node_RHS:
                node_min = self._find_min(node=node.node_RHS)
                node.value = node_min.value
                self.delete(value=node_min.value, node=node_min)
                return

            # The case of existing LHS One-Child
            parent = node.node_parent
            if node.node_LHS:
                if node == self.root:
                    self.root = node.node_LHS
                elif node == parent.node_LHS:
                    parent.node_LHS = node.node_LHS
                    node.node_LHS.node_parent = parent
                else:
                    parent.node_RHS = node.node_LHS
                    node.node_LHS.node_parent = parent
                return
            # The case of existing RHS One-Child
            if node.node_RHS:
                if node == self.root:
                    self.root = node.node_RHS
                elif node == parent.node_LHS:
                    parent.node_LHS = node.node_RHS
                    node.node_RHS.node_parent = parent
                else:
                    parent.node_RHS = node.node_RHS
                    node.node_RHS.node_parent = parent
                return

            # The case of No-Child
            if node == self.root:
                self.root = None
            elif node == parent.node_LHS:
                parent.node_LHS = None
            else:
                parent.node_RHS = None
            return

    def _find_max(self, node=None):
        if not node:
            node = self.root
        if not self.root:
            raise ValueError("The tree is empty")

        if not node.node_RHS:
            return node
        return self._find_max(node=node.node_RHS)

    def _find_min(self, node=None):
        if not node:
            node = self.root
        if not self.root:
            raise ValueError("The tree is empty")

        if not node.node_LHS:
            return node
        return self._find_min(node=node.node_LHS)

    def traverse_pre_order(self, node=None):
        if not node:
            node = self.root
        if not self.root:
            return []

        result = []

        result.append(node.value)
        if node.node_LHS:
            result += self.traverse_pre_order(node=node.node_LHS)
        if node.node_RHS:
            result += self.traverse_pre_order(node=node.node_RHS)
        return result

    def traverse_in_order(self, node=None):
        if not node:
            node = self.root
        if not self.root:
            return []

        result = []

        if node.node_LHS:
            result += self.traverse_in_order(node=node.node_LHS)
        result.append(node.value)
        if node.node_RHS:
            result += self.traverse_in_order(node=node.node_RHS)
        return result

    def traverse_post_order(self, node=None):
        if not node:
            node = self.root
        if not self.root:
            return []

        result = []
        if node.node_LHS:
            result += self.traverse_post_order(node=node.node_LHS)
        if node.node_RHS:
            result += self.traverse_post_order(node=node.node_RHS)
        result.append(node.value)
        return result

    def traverse_level_order(self):
        result = []
        q = Queue()
        q.enqueue(value=self.root)
        while True:
            if len(q) == 0:
                return result
            node = q.dequeue()
            result.append(node.value)
            if node.node_LHS:
                q.enqueue(value=node.node_LHS)
            if node.node_RHS:
                q.enqueue(value=node.node_RHS)
