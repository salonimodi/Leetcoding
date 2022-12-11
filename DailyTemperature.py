from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = (j - i)
        #             break
        # print(ans)

        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_temp = stack.pop()
                ans[prev_temp] = idx - prev_temp
            stack.append(idx)
        print(ans)
        
s = Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
