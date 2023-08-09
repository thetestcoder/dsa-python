class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def countNodes(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.next)
    
    def get_count(self):
        return self.countNodes(self.head)
    

linkedList = LinkedList()
linkedList.head = Node(1)
second = Node(2)
third = Node(3)

linkedList.head.next = second
second.next = third

print(linkedList.get_count())