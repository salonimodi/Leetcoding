from typing import List


class Solution1:
    def maxOps(self, n, m):
        def dp(start, idx):
            if idx == len(m):
                return 0
            end = len(n) - 1 - (idx - start)

            return max(n[start] * m[idx] + dp(start + 1, idx + 1),
                       n[end] * m[idx] + dp(start, idx + 1))

        return dp(0, 0)


class Solution:
    def maxOps(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                l = dp[i + 1][left + 1]
                r = dp[i + 1][left]
                print(dp)
                print(" l ,r " + str(left) + " " + str(right))
                dp[i][left] = max(mult * nums[left] + l, mult * nums[right] + r)

        return dp[0][0]


S = Solution()
print(S.maxOps([1, 2, 3], [3, 2, 1]))
