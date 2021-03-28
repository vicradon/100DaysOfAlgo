class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index == 0:
            return self.head.val

        targetNode = self.head
        trackedIndex = 0

        while targetNode.next is not None:
            targetNode = targetNode.next
            trackedIndex += 1

            if trackedIndex == index:
                return targetNode.val

        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next

        curNode.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        trackedIndex = 0
        curNode = self.head

        while curNode.next is not None:
            trackedIndex += 1

            if trackedIndex == index:
                newNode = Node(val)
                newNode.next = curNode.next
                curNode.next = newNode
                return

            curNode = curNode.next

        if trackedIndex+1 == index:
            curNode.next = Node(val)

    def deleteAtIndex(self, index: int) -> None:
        if (index == 0):
            newHead = self.head.next
            self.head = newHead

        trackedIndex = 0
        curNode = self.head

        while curNode.next is not None:
            trackedIndex += 1

            if trackedIndex == index:
                curNode.next = curNode.next.next
                return

            curNode = curNode.next

    def toList(self):
        curNode = self.head
        normalList = []
        while curNode.next is not None:
            normalList.append(curNode.val)
            curNode = curNode.next
        normalList.append(curNode.val)

        return normalList


linkedList = SinglyLinkedList()
linkedList.addAtHead(7)
linkedList.addAtHead(2)
linkedList.addAtHead(1)
linkedList.addAtIndex(3, 0)
linkedList.deleteAtIndex(2)
linkedList.addAtHead(6)
linkedList.addAtTail(4)
linkedList.get(4)
linkedList.addAtHead(4)
linkedList.addAtIndex(5, 0)
linkedList.addAtHead(6)

linkedList2 = SinglyLinkedList()
linkedList2.addAtHead(1)
linkedList2.addAtTail(3)
linkedList2.addAtIndex(1, 2)
linkedList2.get(1)
linkedList2.deleteAtIndex(1)
linkedList2.get(1)
print(linkedList2.toList())
