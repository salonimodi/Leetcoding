from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        res = []
        d = defaultdict(int)
        arr = [[] for i in range(len(nums)+1)]

        for val in nums:
            d[val] += 1

        for key, value in d.items():
            arr[value].append(key)

        for i in range(len(nums), 0, -1):
            for n in arr[i]:
                if len(res) < k:
                    res.append(n)
                else:
                    return res

        return res





S = Solution()
nums = [-1, -1]
k = 1
print(S.topKFrequent(nums, k))
