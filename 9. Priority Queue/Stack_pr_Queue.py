from heapq import *
count = 0

class Stack_pr_queue:
    def __init__(self) -> None:
        self.heap = []
        heapify(self.heap)
    
    def push(self, value):
        global count
        count += 1
        heappush(self.heap, (-1 * count, value))
    def pop(self):
        return heappop(self.heap)[1]
    


stk = Stack_pr_queue()
stk.push(25)
stk.push(23)
stk.push(20)

print(stk.pop())
print(stk.pop())
print(stk.pop())