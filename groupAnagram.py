from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))

            m[sorted_word].append(word)

        res = []

        for k in m:
            res.append(m[k])

        return res

S = Solution()
print(S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))