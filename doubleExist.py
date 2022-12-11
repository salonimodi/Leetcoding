from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr[i] != 0:
                return True
            elif arr[i] == 0:
                count += 1
        if count > 1:
            return True
        else:
            return False


S = Solution()
print(S.checkIfExist([-2,0,10,-19,4,6,-8]))