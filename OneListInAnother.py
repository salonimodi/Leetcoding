class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


def findList(node_a, node_b):
    

node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(1)
node_b.next.next.next = Node(2)
node_b.next.next.next.next = Node(3)
node_b.next.next.next.next.next = Node(4)

findList(node_a, node_b)