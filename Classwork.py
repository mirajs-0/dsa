# # Creating Class for Nodes in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# # Creating nodes
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# # Linking the nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# def print_node(head):
#     current_node = node1
#     while current_node:
#         print(current_node.data, end = '->')
#         current_node = current_node.next
#     print("null")

# print_node(node1)


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

llist = LinkedList(["a", "b", "c", "d", "e"])

for node in llist:
    print(node)

# # Creating nodes   
# a = Node("a")
# b = Node("b")
# c = Node("c")

# # Linking nodes
# a.next = b
# b.next = c
# c.next = None

# linked_list = LinkedList()
# linked_list.head = a

# print(linked_list.__repr__())



