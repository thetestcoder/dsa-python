class EmptyQueueException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self)

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
    
        
queue = ArrayQueue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
print(queue.is_empty())
print(len(queue))
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.is_empty())
print(len(queue))
queue.enqueue(80)
queue.enqueue(90)
queue.enqueue(100)
print(queue.is_empty())
print(len(queue))