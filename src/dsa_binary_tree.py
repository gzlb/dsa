class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data) -> None:
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left:
                self._insert_recursive(data, current_node.left)
            else:
                current_node.left = Node(data)
        else:
            if current_node.right:
                self._insert_recursive(data, current_node.right)
            else:
                current_node.right = Node(data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def display(self):
        self.inorder_traversal(self.root)
        print()
