from collections import deque


def threeSumMin(nums, target):
            n = len(nums)
            nums.sort()
            count = 0
            for i in range(n-2):
                lo = i+1
                hi = n-1
                while lo < hi:
                    if nums[i] + nums[lo] + nums[hi] < target:
                        count += hi - lo
                        lo += 1
                    else:
                        hi -= 1
            print(count)


threeSumMin([-2, 0, 1, 2, 3], 2)


    # n = len(nums)
    # possibleSol = []
    # for i in range(len(nums)):
    #     for j in range(i + 1, n):
    #         for k in range(j + 1, n):
    #             if target - nums[i] - nums[j] - nums[k] > 0:
    #                 possibleSol.append([nums[i], nums[j], nums[k]])
    # print(possibleSol)

    # nums = deque([('0000', 0)])
    # a, b = nums.popleft()
    # print(a)
    # print(b)

#     for i in range(4):
#         for digit in
#
#
# threeSumMin([1, 2, 3], 2)

