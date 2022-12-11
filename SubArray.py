# def abc():
#     nums = [1]
#     k = 0
#     return 0 if len(nums) == 1 and nums[0] != k else 1
#     count = 0
#     j = 0
#     for i in range(len(nums)):
#         print(sum(nums[j:i+1]))
#         if sum(nums[j:i+1]) > k:
#             j += 1
#         if sum(nums[j:i+1]) == k or nums[i] == k:
#             count += 1
#     return count
#
#
# print(abc())
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            if len(nums) == 1 and nums[0] != k:
                return 0
            else:
                return 1
            count = 0
            j = 0
            for i in range(len(nums)):
                if sum(nums[j:i+1]) > k:
                    j += 1
                if sum(nums[j:i+1]) == k or nums[i] == k:
                    count += 1
            return count
