class sol:
    def lis(self, a):
        LIS = [1] * len(a)
        for i in range(len(a) - 1, -1, -1):
            for j in range(i + 1, len(a)):
                if a[i] < a[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        print(max(LIS))


a = [8, 1, 2, 4, 3]
s = sol()
s.lis(a)
