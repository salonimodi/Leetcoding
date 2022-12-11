from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        flag = False
        for i in range(n-1):
            if flag:
                flag = False
                continue
            if arr[i] == 0:
                temp = arr[i+1:n-1]
                arr[i+1] = 0
                arr[i+2:] = temp
                flag = True
        return arr


S = Solution()
print(S.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))

