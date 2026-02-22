class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise(ValueError)
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current_node = self._root_node
        
        while current_node:
            if data == current_node.data:
                return current_node  # Find the node with the data
            elif data < current_node.data:
                current_node = current_node._left_child  # Move to the left child
            else:
                current_node = current_node._right_child  # Move to the right child
        
        return None  # If data not found in the tree