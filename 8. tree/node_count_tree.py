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
    
    def nodeCount(self, root):
        queue = []
        queue.append(root)
        count = 1
        while len(queue):
            node = queue.pop()
            if node.left is not None:
                count += 1
            if node.right is not None:
                count += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            
        return count

        


values = []

root = TreeNode(1)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(8)

print(root.nodeCount(root))