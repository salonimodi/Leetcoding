from typing import Optional

from LinkedListCreate import LinkedList
from main import getCount


def getCount(head: LinkedList) -> int:
    count = 0
    while head is not None:
        count += 1
        head = head.next
        return count


def getIntersectionNode(headA: LinkedList, headB: LinkedList) -> Optional[LinkedList]:
    headACount = getCount(headA)
    headBCount = getCount(headB)
    if headACount > headBCount:
        for i in range(headACount):
            headA = headA.next
    elif headBCount > headACount:
        for i in range(headBCount):
            headB = headB.next
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next


def Print(node):
    if node == None:
        print("None")
    while node.next != None:
        print(node.data, end="->")
        node = node.next
    print(node.data)


if __name__ == "__main__":
    head1 = LinkedList()
    head1.data = 10
    head2 = LinkedList()
    head2.data = 3
    newNode = LinkedList()
    newNode.data = 6
    head2.next = newNode
    newNode = LinkedList()
    newNode.data = 9
    head2.next.next = newNode
    newNode = LinkedList()
    newNode.data = 15
    head1.next = newNode
    head2.next.next.next = newNode
    newNode = LinkedList()
    newNode.data = 30
    head1.next.next = newNode
    head1.next.next.next = None
    intersect_node = None

    intersect_node = getIntersectionNode(head1, head2)

    print("INTERSECTION LIST :", end="")

    Print(intersect_node)
