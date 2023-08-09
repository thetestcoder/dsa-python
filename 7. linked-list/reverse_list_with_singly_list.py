class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseList(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next


linkedList = LinkedList()
linkedList.head = Node(1)
second = Node(2)
third = Node(3)

linkedList.head.next = second
second.next = third

linkedList.reverseList()
linkedList.printList()