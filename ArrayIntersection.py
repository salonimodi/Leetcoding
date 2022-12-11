from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    j = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and nums[j] % 2 != 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[j] % 2 == 0:
            j += 1
    print(nums)


sortArrayByParity([3, 1, 2, 4])
