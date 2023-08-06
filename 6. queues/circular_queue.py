class CircularQueue:
    def __init__(self):
        self.queue = list()
        self.max_size = int(input("Enter the size of circular queue"))
        self.first = 0
        self.last = 0

    def findsize(self):
        if self.last >= self.last:
            size = self.last - self.first
        else:
            size = self.max_size - (self.first - self.last)
        return size
    
    def displayQ(self):
        print(self.queue)
    
    def enqueue(self, new_element):
        if self.findsize() == (self.max_size - 1):
            print("element cant be enuqued due to queue is full")
        else:
            self.queue.append(new_element)
            self.last = (self.last +1) % self.max_size

    def dequeue(self):
        if self.findsize == 0:
            print("queue is empty")
        else:
            element = self.queue[self.first]
            self.first = (self.first + 1) % self.max_size
        

queue = CircularQueue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.displayQ()
print(queue.findsize())
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.displayQ()
print(queue.findsize())
queue.enqueue(80)
queue.enqueue(90)
queue.enqueue(100)
queue.displayQ()
print(queue.findsize())