def findMaxWages(a, b, N, maxSet = []):
    if N < 0:
        print(maxSet)
        return 0
    if a[N] > b[N]:
        maxSet.insert(0, "a")
    else:
        maxSet.insert(0, "b")
    return findMaxWages(a, b, N - 1, maxSet) + max(a[N], b[N])


a = [1, 34, 3, 234, 22]
b = [23, 345, 23, 68, 28]

28+ 234+ 23+ 345+ 23
print(findMaxWages(a, b, 4))
