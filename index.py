from typing import List


def removeDigit(number: str, digit: str) -> str:
    res = 0
    for i, c in enumerate(number):
        if c == digit:
            if int(res) < int(number[:i] + number[i + 1:]):
                res = number[:i] + number[i + 1:]
    return res


# print(removeDigit("133235", "3"))


def minimumCardPickup(cards: List[int]) -> int:
    d = {}
    prev = len(cards)
    flag = False
    for idx, c in enumerate(cards):
        if c not in d:
            d[c] = idx
        else:
            if idx - d[c] + 1 < prev:
                prev = idx - d[c] + 1
                flag = True
            d[c] = idx
    if flag:
        return prev
    else:
        return -1


# print(minimumCardPickup([1, 2, 3, 4, 5, 6, 7, 5, 8, 5, 9, 1, 2, 3, 4]))


def appealSum(s: str) -> int:
    addition = 0
    for i in range(1, len(s)):
        for j in range(len(s)):
            addition += i
    return addition


# print(appealSum("abc"))
#  a b c ab bc ac abc

def forLoopPractice():
    s = "abc"
    for i in range(1, len(s)+1):
        for j in range(i):
            # print(i)
            pass
#     1 2 2 3 3 3
    windowSize = []
    for i in range(len(s)):
        windowSize.append(i)
        # print(windowSize)
    for i in windowSize:
        for j in range(len(s)):
            print(s[j:i+1])
            pass
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            # print(j)
            pass

    st = set()
    for i in range(len(s)):

        # Iterate from the end of the string
        # to generate substrings
        for j in range(len(s), i, -1):
            sub_str = s[i: i + j]
            st.add(sub_str)

            # Drop kth character in the substring
            # and if its not in the set then recur
            for k in range(1, len(sub_str)):
                sb = sub_str

                # Drop character from the string
                sb = sb.replace(sb[k], "")
                subsequence(sb)



forLoopPractice()
#
# 1
# 0:1 1:1 2:1
#
# 2
# 0:2 1:2
#
# 3
# 0:3

