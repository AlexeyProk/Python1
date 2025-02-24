



from collections import deque

#Implement a class    DequeQueue with the following methods:
class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Dequeue empty")
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def print_queue(self):
        print("Queue:",list(self.queue))

queue = DequeQueue()  #Test it

queue.enqueue(15)
queue.enqueue(40)
queue.enqueue(70)
queue.enqueue(100)
queue.enqueue(147)

queue.print_queue()
print("Dequeued item:", queue.dequeue())
queue.print_queue()

print("Size of the queue:", queue.size())
print("Is the queue empty?", queue.is_empty())

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

print("Is the queue empty?", queue.is_empty())
queue.print_queue()

print("Dequeued item:", queue.dequeue())