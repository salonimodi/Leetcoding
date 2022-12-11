from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        return sum(salary[1:n-1]) / (n-2)


S = Solution()
print(S.average([4000, 3000, 1000, 2000]))