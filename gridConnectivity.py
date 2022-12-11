
# Number of islands in grid

def islandOnGRid(row, col, graph):
    visited = set()
    count = 0
    for r in range(row):
        for c in range(col):
            if explore(r, c, graph, visited):
                count += 1
    print(graph)
    return count


def explore(r, c, graph, visited):
    rowBound = 0 <= r < len(graph)
    colBound = 0 <= c < len(graph[0])
    if not rowBound or not colBound:
        return False
    # if r <= 0 or r > len(graph)-1:
    #     return False
    # if c <= 0 or c > len(graph[0])-1:
    #     return False
    if (r, c) in visited:
        return False
    visited.add((r, c))

    if graph[r][c] != 1:
        return False

    # if 0 < r < len(graph)-1 and 0 < c < len(graph[0])-1:
    #     graph[r][c] = None

    explore(r+1, c, graph, visited)
    explore(r, c+1, graph, visited)
    explore(r-1, c, graph, visited)
    explore(r, c-1, graph, visited)

    return True



graph = [[1, 0, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [0, 1, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1]]

row = len(graph)
col = len(graph[0])

print(islandOnGRid(row, col, graph))
