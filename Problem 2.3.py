from collections import deque


# create a class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) # that is how you add an item tot enqueue

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeu from empty queue")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

print("Deque item: ", queue.dequeue())
print("Size of the queue is ", queue.size())

print ("Is the queue empty? ", queue.is_empty())

