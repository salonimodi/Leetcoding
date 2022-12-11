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


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def mainFunc():
    graph = [1, 8, 2, 5]
    dag = Dag(graph)
    visited = set()
    for key in dag.keys():
        size = dfs(visited, dag, key)


if __name__ == '__main__':
    mainFunc()
