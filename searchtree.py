class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, value):
        self.root = self._insert(self.root, value)
        
    def _insert(self, node, value):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)
        
        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)
        
        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
