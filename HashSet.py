class MyHashSet:
    def __init__(self):
        self.hashList = []

    def add(self, key):
        if key in self.hashList:
            return
        else:
            self.hashList.append(key)
        self.printList()

    def contains(self, key) -> bool:
        if key in self.hashList:
            return True
        else:
            return False

    def remove(self, key):
        if key in self.hashList:
            self.hashList.remove(key)
        self.printList()

    def printList(self):
        print("print")
        for v in self.hashList:
            print(v)


if __name__ == "__main__":
    ml = MyHashSet()
    ml.add(2)
    ml.add(1)
    print(ml.contains(2))
    print("set")
    ml.remove(2)
    print(ml.contains(2))
    print("set")
