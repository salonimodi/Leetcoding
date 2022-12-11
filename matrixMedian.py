def median(matrix, R, C):
    # code here
    res = []
    for r in range(R):
        for c in range(C):
            res.append(M[r][c])
    res.sort()
    print(res)
    n = R * C // 2
    print(res[n])


R = 3
C = 3
M = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
median(M, R, C)