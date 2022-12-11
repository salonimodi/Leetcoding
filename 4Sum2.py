from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dc1 = defaultdict(lambda: 0)
        for a in nums1:
            for b in nums2:
                dc1[a + b] += 1
                # print(a)
                # print(b)
                # print(dc1)
        ans = 0
        print(dc1)
        for c in nums3:
            for d in nums4:
                ans += dc1[-(c + d)]
                print(ans)
                print(dc1)
        return ans


S = Solution()
print(S.fourSumCount([-1, 1, 1, 1, -1], [0, -1, -1, 0, 1], [-1, -1, 1, -1, -1], [0, 1, 0, -1, -1]))
