class EmptyError(Exception):
      def __init__(self, message="Stack is Empty"):
        self.message = message
        super().__init__(self.message)


class ArrayStack:
    def __init__(self) -> None:
        self._data = []
    
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise EmptyError()
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise EmptyError()
        return self._data.pop()
    

myStack = ArrayStack()

print(len(myStack))
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(len(myStack))
print(myStack.pop())
print(myStack.is_empty())
print(myStack.pop())
print(myStack.is_empty())
print(myStack.pop())
print(myStack.is_empty())
print(myStack.pop()) # it will throw an error