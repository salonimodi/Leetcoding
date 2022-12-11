def maxGroupSize( arr, K):
    d = {}
    maxLen = 0
    for i in range(len(arr)):
        if i not in d.keys():
            d[i] = []
            d[i].append(i)
        for j in range(i + 1, len(arr)):
            if (sum(d[i]) + arr[j]) % K != 0:
                d[i].append(arr[j])
                maxLen = max(maxLen, len(d[i]))

    print(maxLen)


maxGroupSize([1,6,7,2],8)