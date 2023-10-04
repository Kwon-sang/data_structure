from linked_list import SinglyLinkedList, DoublyLinkedList
from node import PriorityNode


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, value):
        self.queue.insert(value=value, index=self.queue.size)

    def dequeue(self):
        return self.queue.remove(index=0)

    def __len__(self):
        return self.queue.size


class PriorityQueue:
    def __init__(self):
        self.queue = SinglyLinkedList()

    def enqueue(self, value, priority):
        idx_insert = 0
        for i in range(len(self.queue)):
            node = self.queue.get_node(index=i)
            if priority > node.value.priority:
                idx_insert = i
                break
            else:
                idx_insert += 1
        self.queue.insert(value=PriorityNode(value=value, priority=priority), index=idx_insert)

    def dequeue(self):
        return self.queue.remove(index=0).value


class BinaryHeapQueue:
    def __init__(self):
        self.arr_value = []
        self.arr_priority = []
        self.size = 0

    def enqueue(self, value, priority):
        self.arr_value.append(value)
        self.arr_priority.append(priority)
        self.size = self.size + 1
        self._percolate_up(self.size - 1)

    def _percolate_up(self, idx_percolate):
        if idx_percolate == 0:
            return

        idx_parent = (idx_percolate - 1) // 2
        if self.arr_priority[idx_percolate] > self.arr_priority[idx_parent]:
            self.arr_priority[idx_percolate], self.arr_priority[idx_parent] = \
                self.arr_priority[idx_parent], self.arr_priority[idx_percolate]
            self.arr_value[idx_percolate], self.arr_value[idx_parent] = \
                self.arr_value[idx_parent], self.arr_value[idx_percolate]
            self._percolate_up(idx_parent)

    def dequeue(self):
        if self.size == 0:
            return None

        value = self.arr_value[0]
        self.arr_priority[0] = self.arr_priority[self.size - 1]
        self.arr_value[0] = self.arr_value[self.size - 1]
        self.size -= 1
        self._percolate_down(0)
        return value

    def _percolate_down(self, idx_percolate):
        if self.size <= 2*idx_percolate + 1:  # left node does not exist
            return
        else:
            idx_left_child = 2 * idx_percolate + 1
            left_priority = self.arr_priority[idx_left_child]

        if self.size <= 2*idx_percolate + 2:  # right node does not exist
            right_priority = -99999
            idx_right_child = idx_left_child
        else:
            idx_right_child = 2*idx_percolate + 2
            right_priority = self.arr_priority[idx_right_child]

        idx_bigger_child = idx_left_child if left_priority > right_priority else idx_right_child

        if self.arr_priority[idx_bigger_child] > self.arr_priority[idx_percolate]:
            self.arr_priority[idx_bigger_child], self.arr_priority[idx_percolate] = \
                self.arr_priority[idx_percolate], self.arr_priority[idx_bigger_child]
            self.arr_value[idx_bigger_child], self.arr_value[idx_percolate] = \
                self.arr_value[idx_percolate], self.arr_value[idx_bigger_child]
            self._percolate_down(idx_bigger_child)

    def build(self, arr_input_priority, arr_input_value):
        for i in range(len(arr_input_priority)):
            self.arr_priority[i] = arr_input_priority[i]
            self.arr_value[i] = arr_input_value[i]
        self.size = len(arr_input_priority)
        for i in range(self.size - 1, -1, -1):
            self._percolate_down(i)
