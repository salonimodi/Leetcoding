from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = down = 0
        count = 0
        i = 0
        while i < len(arr):
            while arr[i] <= arr[i+1]:
                up = 1
                count += 1
                i += 1
            while arr[i] >= arr[i+1]:
                down = 1
                count += 1
                i += 1
        if up == 1 and down == 1 and count



S = Solution()
print(S.validMountainArray([0, 3, 2, 1]))