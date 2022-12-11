from typing import List


class Solution:
    @staticmethod
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num not in d:
                d[num] = idx
            else:
                if idx - d[num] <= k:
                    return True
                else:
                    d[num] = idx
        return False


print(Solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
