from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxLen = max(maxLen, count)
                count = 0
                ab
        return max(maxLen, count)

S = Solution()
print(S.findMaxConsecutiveOnes([1,1,0,1,1,1]))