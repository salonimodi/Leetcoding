class Solution:
    def gridTravelPaths(self, n, m):
        if n <= 0 or m <= 0:
            return 0
        if n == 1 or m == 1:
            return 1
        count = 0
        for n in range(n+1):
            for m in range(m+1):
                count = self.gridTravelPaths(n, m-1) + self.gridTravelPaths(n-1, m)
        return count


s = Solution()
print(s.gridTravelPaths(2, 2))