class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, ch in enumerate(s):
            if ch not in d:
                d[ch] = idx
            else:
                d[ch] = None

        for key in d.keys():
            if d[key] is not None:
                return d[key]

        return -1


s = Solution()
print(s.firstUniqChar('leetcode'))