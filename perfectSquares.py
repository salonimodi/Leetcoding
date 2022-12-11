import math
from collections import defaultdict, deque


def perfectSquare(n):
    # sqroot = []
    # for i in range(1, n):
    #     # root = int(math.sqrt(i))
    #     # if root * root == i:
    #     if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)):
    #         sqroot.append(i)
    # adjList = defaultdict(list)
    # lastkey = 0
    # for keys in sqroot:
    #     if keys <= n:
    #         # for vals in sqroot:
    #         #     if vals <= n:
    #         adjList[keys] = sqroot
    #         lastkey = keys
    # q = deque([(lastkey, 0, 0)])
    # seen = set()
    # seen.add(lastkey)
    # while q:
    #     cand, summation, numOfRoots = q.popleft()
    #     if summation == n:
    #         return numOfRoots
    #     for nx in adjList[cand]:
    #         if nx not in seen:
    #             seen.add(nx)
    #             q.append((nx, summation + nx, numOfRoots + 1))
    #
    # return -1

    sqroot = []
    for i in range(1, n+1):
        if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)):
            sqroot.append(i)
    q = deque([(n, 1)])
    seen = set()
    seen.add(n)
    while q:
        cand, numOfRoots = q.popleft()
        if cand in sqroot:
            return numOfRoots
        for nums in sqroot:
            if cand <= nums:
                break
            if cand - nums not in seen:
                seen.add(cand - nums)
                q.append((cand - nums, numOfRoots + 1))


print(perfectSquare(1))
