class Solution:
    def __init__(self, N):
        self.l = []

    def insert(self, pos, ele):
        self.l.insert(pos, ele)

    def printList(self):
        print(self.l)

    def remove(self, ele):
        if ele in self.l:
            self.l.remove(ele)

    def append(self, ele):
        self.l.append(ele)

    def sort(self):
        self.l.sort()

    def lastEleRemove(self):
        self.l.pop()

    def reverseList(self):
        self.l.reverse()


if __name__ == '__main__':
    N = int(input())
    sol = Solution(N)
    for i in range(N):
        cmd = []
        cmd = list(input().split(' '))
        if cmd[0] == 'insert':
            sol.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            sol.printList()
        elif cmd[0] == 'reverse':
            sol.reverseList()
        elif cmd[0] == 'pop':
            sol.lastEleRemove()
        elif cmd[0] == 'append':
            sol.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            sol.sort()
        elif cmd[0] == 'remove':
            sol.remove(int(cmd[1]))



