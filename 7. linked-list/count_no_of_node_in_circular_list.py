class ListItem:
    def __init__(self, value, nextItem = None):
        self.value = value
        self.next = nextItem
    def next(self):
        return self.next
    

class CircularList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, index, value):
        if self.head == None:
            if index != 0: raise Exception("Invalid Index")
            self.head = ListItem(value)
            self.head.next = self.head
        elif index > self.length: raise Exception("Invalid Index")
        elif index == self.length:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = ListItem(value, self.head)
        else:
            temp = self.head
            for _ in range(index -1):
                temp = temp.next
            temp2 = temp.next
            temp.next = ListItem(value, temp2)
        self.length += 1
    
    def append(self, value):
        self.insert(self.length, value)
    
    def size(self):
        if self.head is None:
            return 0
        ans = 1
        temp = self.head.next
        while temp is not self.head:
            temp = temp.next
            ans += 1
        return ans
    
    def print(self):
        print(self.head.value, end=' ')
        temp = self.head.next
        while temp != self.head:
            print(temp.value, end = ' ')
            temp = temp.next
        print()
    

cl1 = CircularList()
cl1.append(1)
cl1.append(2)
cl1.append(4)
print(cl1.size())
cl1.print()