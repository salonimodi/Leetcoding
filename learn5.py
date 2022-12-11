import operator
if __name__ == '__main__':
    hashSet = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        hashSet[name] = score

    secondLow = list(set(sorted(hashSet.values(), key = lambda x:float(x), reverse=True)))
    print(secondLow)
    res = []
    for key in hashSet:
        if hashSet[key] == secondLow:
            res.append(key)

    print(sorted(res))


