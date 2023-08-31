class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
            
root = Node(30)

insert(root, Node(24))
insert(root, Node(58))
insert(root, Node(48))
insert(root, Node(26))
insert(root, Node(11))
insert(root, Node(13))