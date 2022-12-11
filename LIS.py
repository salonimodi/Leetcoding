def Dag(graph):
    d = {}
    for i in range(len(graph)):
        if graph[i] not in d.keys():
            d[graph[i]] = []
        for j in range(i + 1, len(graph)):
            if graph[j] > graph[i]:
                d[graph[i]].append(graph[j])
    print(d)
    return d


def visitNeighbour(node, dag, visited) -> int:
    if len(dag[node]) == 0:
        return 0
    size = 0
    val = []
    if node not in visited:
        size = 1
        for neighbour in dag[node]:
            val.append(size)
            visited.add(node)
            size += visitNeighbour(neighbour, dag, visited)
    return size


def LIS(graph):
    visited = set()
    dag = Dag(graph)
    lis = 0
    for key in dag:
        for node in dag[key]:
            size = visitNeighbour(node, dag, visited)
        if size > lis:
            lis = size
    print(lis)


graph = [1, 8, 2, 5]

print(graph)
LIS(graph)
