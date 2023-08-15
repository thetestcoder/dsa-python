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
    
    def delete(self, node, value):
        if node is None:
            return node
        if node.value  == value:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                while node.left is not None:
                    node = node.left
                node.right =  self.delete(node.right, node.value)
        elif value < node.value:
            node.left = self.delete(node.left, node.value)
        else:
            node.right = self.delete(node.right, node.value)
        return node
    
    def printPreOrder(self):
        if self:
            print(self.value)
            if self.left is not None:
                self.left.printPreOrder()
            if self.right is not None:
                self.right.printPreOrder()

    def printPostOrder(self):
        if self:
            if self.left is not None:
                self.left.printPostOrder()
            if self.right is not None:
                self.right.printPostOrder()
            print(self.value)
    
    def printInOrder(self):
        if self:
            if self.left is not None:
                self.left.printInOrder()
            print(self.value)
            if self.right is not None:
                self.right.printInOrder()
    

root  = TreeNode(1)
root.insert(4)
root.insert(3)
root.insert(5)
root.insert(6)
root.insert(10)
print("Print In Order ============ ")
root.printInOrder()

new_tree = root.delete(root, 1)
print("Print Pre Order =========== ")
new_tree.printPreOrder()