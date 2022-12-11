from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = 0
        direction = 'down'
        n = len(nums)
        for i in range(n - 1):
            if direction == 'down' and nums[i] >= nums[i + 1]:
                ans += nums[i]
                direction = 'up'
            elif direction == 'up' and nums[i] <= nums[i + 1]:
                ans -= nums[i]
                direction = 'down'
        if direction == 'up':
            return ans
        return ans + nums[-1]


nums = [4, 2, 5, 9]
S = Solution()
print(S.maxAlternatingSum(nums))
