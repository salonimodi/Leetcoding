class CircularQueue:
    def __init__(self, size):
        self.front = self.rear = -1
        self.maxSize = size
        self.queue = [None] * size
        self.currentSize = 0

    def enQueue(self, element) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (1 + self.rear) % self.maxSize
        self.queue[self.rear] = element
        self.currentSize += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (1 + self.front) % self.maxSize
        self.currentSize -= 1
        return True

    def isFull(self) -> bool:
        if self.currentSize == self.maxSize:
            return True
        return False

    def isEmpty(self) -> bool:
        if self.currentSize == 0:
            return True
        return False

    def getRear(self) -> int:
        return self.queue[self.rear]

    def getFront(self) -> int:
        return self.queue[self.front]


# c = CircularQueue(3)
# print(c.isEmpty())
# print(c.isFull())
# print(c.enqueue(1))
# print(c.enqueue(2))
# print(c.getFront())
# print(c.getRear())
# print(c.dequeue())
# print(c.enqueue(3))
# print(c.enqueue(4))
# print(c.enqueue(5))
# print(c.isFull())
# print(c.isEmpty())
# print(c.getFront())
# print(c.getRear())

myCircularQueue = CircularQueue(3)
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(4))
print(myCircularQueue.getRear())
print(myCircularQueue.isFull())
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(4))
print(myCircularQueue.getRear())
