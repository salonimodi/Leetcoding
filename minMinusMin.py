from typing import List


class Solution:

    def removals(self, a, n, k) -> List:
        a.sort()
        i = 1
        j = 0
        maxLen = 0
        while i < n:
            if a[i] - a[j] <= k:
                maxLen = max(maxLen, i - j + 1)
            else:
                j += 1
            i += 1

        if n - maxLen == 0:

        else:
            return n - maxLen
        # a.sort()
        # maxLen = 0
        # i = 0
        # for j in range(i + 1, n):
        #     if a[j] - a[i] <= k:
        #         maxLen = max(maxLen, j - i + 1)
        #     else:
        #         i = i + 1
        #
        #     if i >= n:
        #         break
        # remove = n - maxLen
        # print(remove)



K = 11
arr = [62, 24]
s = Solution()
s.removals(arr, len(arr), K)
