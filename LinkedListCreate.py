class LinkedList:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedListOps:

    def __init__(self):
        self.head = None

    def printLinkedList(self):
        n = self.head
        while n is not None:
            print(n.val)
            n = n.next

    def addNodeAtBeginning(self, val):
        node = LinkedList(val)
        node.next = self.head
        self.head = node

    def removeNodeFromBeginning(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next


class Operations:
    if __name__ == "__main__":
        linkedList = LinkedListOps()
        linkedList.addNodeAtBeginning(10)
        linkedList.addNodeAtBeginning(20)
        linkedList.addNodeAtBeginning(30)
        linkedList.printLinkedList()
        linkedList.removeNodeFromBeginning()
        print("linked List after removing")
        linkedList.printLinkedList()
