# from collections import defaultdict
#
# nums = []
# visited = set()
# deadends = set(["0101"])
# for i in range(10):
#     cand = "0000" + str(i)
#     nums.append(cand[-4:])
#
# adjList = defaultdict(list)
# for cand in nums:
#     for i in range(4):
#         for digit in [((int(cand[i]) + 1) % 10), ((int(cand[i]) - 1) % 10)]:
#             print(cand[:i])
#             print(str(digit))
#             print(cand[i + 1:])
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        count = 0
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                # count += 1
                # dp[i][left] = count
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1],
                                  mult * nums[right] + dp[i + 1][left])
        print(dp)


S = Solution()
S.maximumScore([1, 2, 3], [3, 2, 1])

