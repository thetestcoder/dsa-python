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
    
    def find_middle(self):
        temp1 = self.head
        temp2 = self.head

        while (temp1 is not None) and (temp1.next.next is not None):
            temp1 = temp1.next.next
            temp2 = temp2.next
        print(temp2.data)


print("==========================================")
print("===========List 1================")
linkedList1 = LinkedList()
linkedList1.insert("Deep")
linkedList1.insert("Monika")
linkedList1.insert("Kavya")
linkedList1.insert("Garima")
linkedList1.find_middle()

