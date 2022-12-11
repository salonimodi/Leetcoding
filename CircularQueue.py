class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k 
        self.maxLength = k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.rear == self.maxLength - 1 and self.front != 0:
                self.queue.append(value)
                self.rear += 1
                return True
            else:
                return False
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = self.rear = -1
                return True
            elif self.front == self.maxLength - 1:
                self.front = 0
                return True
        else:
            return False

    def Front(self) -> int:
        return self.front

    def Rear(self) -> int:
        return self.rear

    def isEmpty(self) -> bool:
        if self.front() == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.rear == self.maxLength-1 or self.rear == self.front - 1:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3);
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
print(myCircularQueue.isFull())
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())