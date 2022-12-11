def NoOfChicks(N):
    eachDay = [0] * (N + 1)
    prev = 1
    eachDay[1] = 1
    if N == 1:
        return 1
    for i in range(2, N + 1):
        if i <= 6:
            prev = prev + prev * 2
            eachDay[i] = prev
        if i == 7:
            eachDay[i] = prev + prev * 2 - eachDay[2]
            prev = eachDay[i]
        if i > 7:
            eachDay[i] = prev + prev * 2 - (eachDay[i - 5] - eachDay[i - 6])
            prev = eachDay[i]
    print(prev)
    print(eachDay)


NoOfChicks(9)


class GFG:
    def Solution(self, N):
        if N == 1:
            return 1
        if N <= 6:
            return 3 * self.NoOfChicks(N - 1)
        elif N == 7:
            return 3 * self.NoOfChicks(N - 1) - 3 * self.NoOfChicks(N - 6)
        else:
            return 3 * self.NoOfChicks(N - 1) - 2 * self.NoOfChicks(N - 6)


if '__name__' == '__main__':
    g = GFG()
    k = g.Solution(12)
    print(k)
