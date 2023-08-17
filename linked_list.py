class Node:
    def __init__(self,
                 item=None,
                 next_node:'Node'=None,
                 is_head: bool=False,
                 is_tail: bool=False):
        self.item = item
        self.next_node = next_node
        self.is_head = is_head
        self.is_tail = is_tail


class LinkedList:
    def __init__(self):
        self.node_tail = Node(is_tail=True)
        self.node_head = Node(is_head=True, next_node=self.node_tail)
        self.size = 0

    def get(self, index) -> Node:
        node = self.node_head
        for i in range(index+1):
            node = node.next_node
        return node

    def insert(self, item, index):
        if index < 0 or index > len(self):
            raise IndexError
        node_before = self.get(index-1)
        node_after = node_before.next_node
        node_new = Node(item=item, next_node=node_after)
        node_before.next_node = node_new
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
        node_before = self.get(index - 1)
        node_remove = node_before.next_node
        node_before.next_node = node_before.next_node.next_node
        self.size -= 1
        return node_remove.item

    def items(self) -> list:
        items = []
        node = self.node_head.next_node
        while not node.is_tail:
            items.append(node.item)
            node = node.next_node
        return items

    def __len__(self):
        return self.size


# TEST
if __name__ == '__main__':
    import random

    # 삽입 테스트
    linked_list = LinkedList()
    for i in range(100):
        random_item = random.randrange(1, 100)
        linked_list.insert(item=random_item, index=i)
        assert linked_list.get(linked_list.size-1).item == random_item

    # 삭제 테스트
    for i in range(100):
        random_index = random.randrange(linked_list.size)
        remove_value = linked_list.items()[random_index]
        remove_result = linked_list.remove(index=random_index)
        assert remove_value == remove_result
