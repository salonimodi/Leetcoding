class Solution:
    def longestArr(self, a, k):
        solSet = {}
        maxLen = 0
        for i in range(len(a)):
            reminder = sum(a[:i + 1]) % k
            if reminder != 0 and reminder not in solSet:
                solSet[reminder] = i
                maxLen = i - solSet[reminder] if maxLen < i - solSet[reminder] else maxLen
            else:
                maxLen = i+1 if maxLen < i+1 else maxLen
        return maxLen


if __name__ == "__main__":
    print("Hi There!!")
    l1 = Solution()
    print(l1.longestArr([1, 2, 3, 4, 8, 1, 1, 1], 3))

# arr = [1, 2, 3, 4, 5]
# rem = [1, 1, 0, 0, 1]
# idx = [0, 1, 2, 3, 4]
# set = {1:0}
#
# ans = [i-set[rem] = 1-0=1, i+1= 3, i+1 =4, 4-0=4  ]
# max(ans)

# class Solution:
#     def longestArr(self, a, k):
#         solSet = {}
#         maxLen = []
#         for i in range(len(a)):
#             reminder = sum(a[:i + 1]) % k
#             if reminder != 0 and reminder not in solSet:
#                 solSet[reminder] = i
#             elif reminder == 0:
#                 maxLen.append(i+1)
#             else:
#                 maxLen.append(i - solSet[reminder])
#         print(solSet)
#         print(maxLen)
#         print(reminder)
#         return max(maxLen)
