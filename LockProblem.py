from typing import List


# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         pass
#
#
# deadends = ["0201", "0101", "0102", "1212", "2002"]
# target = "0202"


class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     ans = 0
    #     prev = 0
    #     d = {0:1}
    #
    #     for num in nums:
    #         prev = prev + num
    #         print("pref: " + str(prev))
    #
    #         if prev - k in d:
    #             ans = ans + d[prev - k]
    #
    #         if prev not in d:
    #             d[prev] = 1
    #         else:
    #             d[prev] = d[prev] + 1
    #     print(d)
    #     print(ans)

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        j = 0
        for i in range(len(nums)):
            if sum(nums[:i+1]) > k:
                j += 1
            if sum(nums[j:i+1]) == k:
                count += 1
        print(count)


nums = [-1,0,1]
k = 0
s = Solution()
s.subarraySum(nums, k)
