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
    
    def sumOfNodeValues(self):
       global sum_of_node
       if self:
           sum_of_node += self.value
           if self.left is not None:
               self.left.sumOfNodeValues()
           if self.right is not None:
               self.right.sumOfNodeValues()
       return sum_of_node

        


sum_of_node = 0

root = TreeNode(1)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(8)


print(root.sumOfNodeValues())