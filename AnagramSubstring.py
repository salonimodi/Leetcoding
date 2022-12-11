from typing import List


def findAnagram(searchStr: str, mainStr: str) -> List[int]:
    if len(mainStr) < len(searchStr):
        return []
    sCount, mCount = {}, {}
    for i in range(len(searchStr)):
        sCount[searchStr[i]] = 1 + sCount.get(searchStr[i], 0)
        mCount[mainStr[i]] = 1 + mCount.get(mainStr[i], 0)
    res = [0] if sCount == mCount else []
    left = 1
    print(mCount)
    for right in range(len(searchStr), len(mainStr)):
        mCount[mainStr[right]] = 1 + mCount.get(mainStr[right], 0)
        mCount[mainStr[right]] -= 1
        print(mCount)
        if mCount[mainStr[left]]:
            mCount.pop(mainStr[left])
        left += 1

        if mCount == sCount:
            res.append(left)
    print(res)


findAnagram('abc', 'xyzbacdabcbarew')
