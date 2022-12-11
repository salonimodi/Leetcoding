from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1, numRows + 1):
            row = [1] * i
            lastRow = triangle[-1] if triangle else []
            for j in range(1, len(lastRow)):
                print(len(lastRow))
                print(range(1, len(lastRow)))
                row[j] = lastRow[j - 1] + lastRow[j]
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    print("Hi There!!")
    l1 = Solution()
    print(l1.generate(3))
