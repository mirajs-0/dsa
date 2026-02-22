class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return
                current = current.right

    def _find(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def delete_node(self, data):
        # Find the node to delete
        node = self._find(data)
        if node is None:
            return  # Node not found, nothing to do

        # Small helper to transplant subtrees (shift_nodes equivalent)
        def shift_nodes(u, v):
            """Replace subtree rooted at u with subtree rooted at v."""
            if u.parent is None:
                # u is the root
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v is not None:
                v.parent = u.parent

        # Case 1: Node has no left child
        if node.left is None:
            shift_nodes(node, node.right)

        # Case 2: Node has no right child
        elif node.right is None:
            shift_nodes(node, node.left)

        # Case 3: Node has two children
        else:
            # Find in-order successor (leftmost node in right subtree)
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            if successor.parent != node:
                # Detach successor from its current position
                shift_nodes(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            # Replace node with successor
            shift_nodes(node, successor)
            successor.left = node.left
            successor.left.parent = successor