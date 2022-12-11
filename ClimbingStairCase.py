class Solution:
    # def climbingStairs(self, n):
    #     if n < 0:
    #         return 0
    #     if n == 0 or n == 1:
    #         return 1
    #
    #     return self.climbingStairs(n-1) + self.climbingStairs(n-2)

    def climbingStairs(self, n, memo={}):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.climbingStairs(n - 1, memo) + self.climbingStairs(n - 2, memo)
            return memo[n]


s = Solution()
print(s.climbingStairs(5))
