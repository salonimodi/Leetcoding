class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys() and t[i] not in d.values():
                d[s[i]] = t[i]
            else:
                if s[i] in d and d[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True


S = Solution()
print(S.isIsomorphic("aaeaa", "uuxyy"))