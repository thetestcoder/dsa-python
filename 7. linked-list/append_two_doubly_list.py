class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def insert(self, data):
        if(self.head == None):
            self.end = self.head = Node(data)
        else:
            temp = Node(data)
            temp.prev = self.end
            self.end.next = temp
            self.end = temp
        
    def print_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
    def print_backward(self):
        temp = self.end
        while temp is not None:
            print(temp.data)
            temp = temp.prev
    
    def append_two_lists(self, input_list):
        self.end.next = input_list.head
        input_list.head.prev = self.end
        self.end = input_list.end


print("==========================================")
print("===========List 1================")
linkedList1 = LinkedList()
linkedList1.insert("Deep")
linkedList1.insert("Monika")
linkedList1.print_forward()

print("==========================================")
print("===========List 2================")

linkedList2 = LinkedList()
linkedList2.insert("Kavya")
linkedList2.insert("Garima")
linkedList2.print_forward()

print("==========================================")
print("===========Append two list================")

linkedList1.append_two_lists(linkedList2)
linkedList1.print_forward()