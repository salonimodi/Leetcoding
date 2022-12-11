class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def reverse(self):
        if self.head is None:
            return

        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # def zipperTwoLists(self, listHead_1, listHead_2):
    # resultLIst = LinkedList()
    # while listHead_1 is not None and listHead_2 is not None:



if __name__ == '__main__':
    llist = LinkedList()
    llist.add(20)
    llist.add(4)
    llist.add(15)
    llist.add(85)

    l = LinkedList()
    l.add(40)
    l.add(100)

    llist.printList()
    llist.reverse()
    llist.printList()

    llist.zipperTwoLists(l)




