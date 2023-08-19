from heapq import *
count = 0

class FIFO_pr_Queue:
    def __init__(self) -> None:
        self.heap = []
        heapify(self.heap)
    
    def enqueue(self, value):
        global count
        count += 1
        heappush(self.heap, (count, value))
    def dequeue(self):
        return heappop(self.heap)[1]
    


fifo = FIFO_pr_Queue()
fifo.enqueue(25)
fifo.enqueue(23)
fifo.enqueue(20)

print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())