def satisfyEqn(A, N):
    d = {}
    res = []
    for i in range(N):
        for j in range(i + 1, N):
            sumVal = A[i] + A[j]
            if sumVal not in d:
                d[sumVal] = i, j
            else:
                if i not in d[sumVal] and j not in d[sumVal]:
                    value = [d[sumVal][0], d[sumVal][1], i, j]
                    if len(res) == 0:
                        res.append(value)
                    else:
                        if res[0] > value:
                            res[0] = value
    if len(res) == 0:
        return [-1] * 4
    else:
        print(res[0])


A = [684, 931, 873, 347, 748, 68, 810, 604, 333, 291, 68, 422, 684, 39, 756, 485, 215, 7, 217, 690, 758, 476]
N = len(A)
satisfyEqn(A, N)
