import ctypes


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self, *nodes):
        if nodes:
            self.head = Node(None, None, nodes[0])
            for i in range(0, len(nodes)-1):
                nodes[i].next = nodes[i+1]
                nodes[i+1].prev = nodes[i]

    def insert_node(self, node, pos):
        # pos is the id of the node after which the new node is to be inserted
        prev_node = ctypes.cast(pos, ctypes.py_object).value
        node.next = prev_node.next
        prev_node.next = node

    def delete_node(self, pos):
        # pos is the id of the node that is to be deleted
        prev_node = ctypes.cast(pos, ctypes.py_object).value
        prev_node.next = prev_node.next.next

    def traverse(self):
        node = self.head.next
        while node:
            print(node.data, end=' ')
            node = node.next
        print()


lnkd_lst = LinkedList(Node(1), Node(2), Node(3))

lnkd_lst.traverse()

lnkd_lst.insert_node(Node(4), id(lnkd_lst.head.next.next))

lnkd_lst.traverse()

lnkd_lst.delete_node(id(lnkd_lst.head.next.next))

lnkd_lst.traverse()
