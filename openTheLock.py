from collections import defaultdict, deque


def abc():
    target = '1111'
    nums = []
    visited = set()
    deadends = set(["0101"])

    for i in range(10000):
        cand = "0000" + str(i)
        nums.append(cand[-4:])

    adjList = defaultdict(list)
    for num in nums:
        for i in range(4):
            for digit in [((int(num[i])+1) % 10), ((int(num[i])-1) % 10)]:
                nx = num[:i] + str(digit) + num[i+1:]
                if nx not in deadends:
                    adjList[num].append(nx)

    q = deque([("0000", 0)])
    while q:
        cand, step = q.popleft()
        if cand == target:
            return step
        for nx in adjList[cand]:
            if nx not in visited:
                visited.add(nx)
                q.append((nx, step+1))
        print(q)
    return -1


v = abc()
print(v)







