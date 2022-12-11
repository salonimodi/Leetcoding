from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        nums.sort()
        i = 0
        j = len(nums)-1
        setA = []
        setB = []
        setA.append(nums[i])
        setB.append(nums[j])
        while i < j-1:
            if sum(setA) < sum(setB):
                i += 1
                setA.append(nums[i])
            else:
                j -= 1
                setB.append(nums[j])
        return sum(setA) == sum(setB)


S = Solution()
print(S.canPartition([1, 1, 2, 2]))