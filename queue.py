from linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, value):
        self.queue.insert(value=value, index=self.queue.size)

    def dequeue(self):
        return self.queue.remove(index=0)

    def __len__(self):
        return self.queue.size
