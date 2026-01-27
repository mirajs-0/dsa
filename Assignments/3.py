# # Creating Class for Nodes in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__ (self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes =[]
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

     # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Insert between two nodes (after a given node)
    def insert_after_node(self, prev_node_data, data):
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        print(f"Node with data '{prev_node_data}' not found.")

    # Remove a node by data
    def remove_node(self, data):
        current_node = self.head
        # If the node to be removed is the head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        prev_node = None
        while current_node:
            if current_node.data == data:
                prev_node.next = current_node.next
                current_node = None
                return
            prev_node = current_node
            current_node = current_node.next
        print(f"Node with data '{data}' not found.")
    
llist = LinkedList(["a", "b", "c", "d", "e"])

print("Initial Linked List:", llist)

# insert at beginning
llist.insert_at_beginning("x")
print("After inserting 'x' at the beginning:", llist)

# insert at end
llist.insert_at_end("f")
print("After inserting 'f' at the end:", llist)

# insert after a specific node
llist.insert_after_node("c", "y")
print("After inserting 'y' after 'c':", llist)

# remove a node
llist.remove_node("b")
print("After removing node 'b':", llist)

# Try removing a non-existent node
llist.remove_node("z")





