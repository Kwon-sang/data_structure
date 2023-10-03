from node import SinglyNode, DoublyNode


class SinglyLinkedList:
    def __init__(self):
        self.node_tail = SinglyNode(is_tail=True)
        self.node_head = SinglyNode(is_head=True, node_next=self.node_tail)
        self.size = 0

    def get_node(self, index):
        node = self.node_head
        for i in range(index + 1):
            node = node.node_next
        return node

    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise IndexError

        node_insert_front = self.get_node(index - 1)
        node_insert_rear = node_insert_front.node_next
        node_insert = SinglyNode(value=value, node_next=node_insert_rear)
        node_insert_front.node_next = node_insert
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError

        node_remove_front = self.get_node(index - 1)
        node_remove = node_remove_front.node_next
        node_remove_front.node_next = node_remove.node_next
        self.size -= 1
        return node_remove.value

    def get_values(self):
        values = []
        node = self.node_head.node_next
        while not node.is_tail:
            values.append(node.value)
            node = node.node_next
        return values

    def __len__(self):
        return self.size


class DoublyLinkedList:
    def __init__(self):
        self.node_head = DoublyNode(is_head=True)
        self.node_tail = DoublyNode(is_tail=True)
        self.size = 0
        self.node_head.node_next = self.node_tail
        self.node_tail.node_prev = self.node_head

    def get_node(self, index):
        if index < self.size // 2:
            return self._get_node_from_head(index=index)
        else:
            return self._get_node_from_tail(index=index)

    def _get_node_from_head(self, index):
        node = self.node_head
        for i in range(index + 1):
            node = node.node_next
        return node

    def _get_node_from_tail(self, index):
        node = self.node_tail
        for i in range(self.size, index, -1):
            node = node.node_prev
        return node

    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise IndexError

        node_insert_front = self.get_node(index - 1)
        node_insert_rear = node_insert_front.node_next
        node_insert = DoublyNode(value=value, node_prev=node_insert_front, node_next=node_insert_rear)
        node_insert_front.node_next = node_insert
        node_insert_rear.node_prev = node_insert
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError

        node_remove_front = self.get_node(index - 1)
        node_remove_rear = node_remove_front.node_next.node_next
        node_remove = node_remove_front.node_next
        node_remove_front.node_next = node_remove_rear
        node_remove_rear.node_prev = node_remove_front
        self.size -= 1
        return node_remove.value

    def get_values(self):
        values = []
        node = self.node_head.node_next
        while not node.is_tail:
            values.append(node.value)
            node = node.node_next
        return values

    def __len__(self):
        return self.size
