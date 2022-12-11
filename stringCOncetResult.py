
class Solution:
    def maxOps(self, target, s):
        n = len(s)
        dp = [[] for _ in range(n)]

        dp[0] = ['']
        for i in range(len(target)):
            for ch in s:
                if target[i] == ch[:1]:
                    t = len(ch)
                    for valuesAtCurrent in dp[i]:
                        dp[i+t].append(valuesAtCurrent + ch)
        print(dp)


S = Solution()
S.maxOps("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])