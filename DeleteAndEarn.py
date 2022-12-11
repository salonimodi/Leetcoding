from collections import defaultdict
from functools import cache
from typing import List


# class Solution:
#
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         d = defaultdict(int)
#         max_number = 0
#         for num in nums:
#             d[num] += num
#             max_number = max(max_number, num)
#         print(d)
#
#         @cache
#         def dp(i):
#             if i == 0:
#                 return 0
#             if i == 1:
#                 return d[1]
#             print(d)
#             return max(d[i] + dp(i - 2), dp(i - 1))
#
#         return dp(max_number)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        # Declare our array along with base cases
        max_points = [0] * (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            # Apply recurrence relation
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])

        return max_points[max_number]


S = Solution()
print(S.deleteAndEarn([5, 4, 5, 4, 3, 8, 3]))

