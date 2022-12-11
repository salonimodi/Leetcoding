from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0 and n > 0:
            nums1 = nums2
            return nums1
        if m > 0 and n > 0:
            p = n + m - 1
            p1 = m - 1
            p2 = n - 1

            for i in range(m + n - 1, 0, -1):
                if nums1[p1] >= nums2[p2]:
                    nums1[p] = nums1[p1]
                    p -= 1
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p -= 1
                    p2 -= 1
            return nums1


S = Solution()
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(S.merge(nums1, m, nums2, n))