from queue import LifoQueue

class CustomQueue(LifoQueue):
    def enqueue(self, val):
       temp_stack = LifoQueue()
       while(self.empty() == False):
           temp_stack.put(self.get())
       self.put(val)
       while(temp_stack.empty() == False):
           self.put(temp_stack.get())

    def dequeue(self):
       return self.get()
    
    def front(self):
        temp = self.get()
        self.put(temp)
        return temp
    

       
customQueue = CustomQueue()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)
print(customQueue.front())
customQueue.dequeue()
customQueue.dequeue()
print(customQueue.front())
customQueue.dequeue()
customQueue.enqueue(50)
customQueue.enqueue(60)
print(customQueue.front())