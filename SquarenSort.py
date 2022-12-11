import math
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums))
        pos = len(nums) - 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] ** 2
                l += 1
                pos -= 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
                pos -= 1
        return res

S =Solution()
print(S.sortedSquares([-4, -1, 0, 3, 10]))