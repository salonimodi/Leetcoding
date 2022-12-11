from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # essentials
        n = len(nums)
        dp = [None] * n

        # base case
        if n == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # for loop to fill dp list
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]

class Sol2:
    def rob(self, nums: List[int]) -> int:

        def dp(i):
            # base case
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            # recurssion to reach till bottom
            if i not in memo:
                memo[i] = max(nums[i] + dp(i-2), dp(i-1))
            return memo[i]
        
        # essential
        memo = {}
        return dp(len(nums) - 1)


S = Solution()
print(S.rob([1, 2, 3, 1]))
