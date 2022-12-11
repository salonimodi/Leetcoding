from typing import List
#
#
# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         d = {}
#         res = []
#         minSum = len(list1) if len(list1) > len(list2) else len(list2)
#         for i in range(len(list1)):
#             d[list1[i]] = i
#
#         for i in range(len(list2)):
#             if list2[i] in d.keys():
#                 if d[list2[i]]+i <= minSum:
#                     res.append(list2[i])
#                     minSum = d[list2[i]]+i

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        common = list(set1 & set2)
        print(common)
        d = {}
        for i in common:
            d[i] = list1.index(i) + list2.index(i)
        print(d)
        min_index = min(d.values())
        op = []
        for i in d:
            if d[i] == min_index:
                op.append(i)
        print(op)
        return op


S = Solution()
# list1 = ["happy", "sad", "good"]
# list2 = ["sad", "happy", "good"]
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
S.findRestaurant(list1, list2)
