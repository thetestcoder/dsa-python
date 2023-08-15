class TreeNode:
    def __init__(self, value: int) -> None:
        self.left = None
        self.right = None
        self.value = value
    
    def treeDepth(self, root):
        if root is None:
            return 0
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        return max(left, right) + 1
        


count = 0

root = TreeNode(1)
root.left= TreeNode(2)
root.right= TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(root.treeDepth(root) - 1)