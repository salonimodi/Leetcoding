def find(parent, n):
    if (parent[n] != n):
        parent[n] = find(parent, parent[n])
    return parent[n]


def union(parent, n, m):
    parent[n] = find(parent, n)
    parent[m] = find(parent, m)
    if (n > m):
        parent[parent[n]] = parent[m]
    else:
        parent[parent[m]] = parent[n]


t = int(input())
for _ in range(t):
    co = int(input())
    parent = [i for i in range(10 ** 5)]
    count_parent = [0 for i in range(10 ** 5)]
    for __ in range(co):
        n, m = map(int, input().split())
        union(parent, n - 1, m - 1)
    for i in range(10 ** 5):
        parent[i] = find(parent, i)
        count_parent[parent[i]] += 1
    print(max(count_parent))

