class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = 0
        d = {}
        pos = -1
        for idx, ch in enumerate(s):
            if ch in d and d[ch] > pos:
                pos = d[ch]
            d[ch] = idx
            sLen = max(sLen, idx - pos)
        print(sLen)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         d = {}
#         pos = -1
#         for idx, ch in enumerate(s):
#             if ch in d and d[ch] > pos:
#                 pos = d[ch]
#             d[ch] = idx
#             res = max(res, idx - pos)
#         print(res)


S = Solution()
S.lengthOfLongestSubstring("abba")