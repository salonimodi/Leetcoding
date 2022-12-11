from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    given = sorted(nums)
    for i in range(len(given)):
        possileSol = sum(given[i:i+3])
        if possileSol == target:
            res.append([nums[:i+1]])
    return res


print(fourSum([-1, 2, 0, 1, -2], 0))
