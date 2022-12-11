class Solution:
    def smallestStr(self, S, P):
        len_S = len(S)
        len_P = len(P)
        if len_P == 0 or len_S == 0 or len_P > len_S:
            return ""
        want = {}
        dct = {}

        for ch in t:
            dct[ch] = dct.get(ch, 0) + 1
        minLen = 0
        requiredStr = ""

        for i in range(len(S)):
            if S[i] in P:
                if S[i] in want:
                    want[S[i]] = want[S[i]] + 1
                else:
                    want[S[i]] = 1
            if want.values()
                requiredStr += S[i]
        print(want)
        print(requiredStr)

if __name__ == "__main__":
    print("Hi There!!")
    l1 = Solution()
    l1.smallestStr("salonimodai", "oi")


# want = {a:1, b:0, c:0}
