class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.val = val

def mergeTwoList(l1, l2):
    temp = l1
    while l1.next is not None:
        l1 = l1.next
    l1.next = l2
    while temp is not None:
        print(temp.val)
        temp = temp.next
    
first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third

first2 = Node(4)
second2 = Node(5)
third2 = Node(6)
first2.next = second2
second2.next = third2

mergeTwoList(first, first2)