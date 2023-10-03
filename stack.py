from linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.stack = DoublyLinkedList()

    def push(self, value):
        self.stack.insert(value=value, index=self.stack.size)

    def pop(self):
        return self.stack.remove(index=self.stack.size-1)

    def __len__(self):
        return self.stack.size
