class TreeNode:
    def __init__(self, value: int) -> None:
        self.left = None
        self.right = None
        self.value = value
    def insert(self, value: int):
        if self.value:
            if value <= self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
    
    def PreOrderTranversal(self):
        global values
        if self:
            values.append(self.value)
            if self.left is not None:
                self.left.PreOrderTranversal()
            if self.right is not None:
                self.right.PreOrderTranversal()
            return values
    
    def newTreePreOrderPrint(self):
        print(self.value)
        if self.left is not None:
            self.left.newTreePreOrderPrint()
        if self.right is not None:
            self.right.newTreePreOrderPrint()



values = []

root = TreeNode(1)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(8)

root.PreOrderTranversal()
print(values)
new_tree = root
new_tree.newTreePreOrderPrint()