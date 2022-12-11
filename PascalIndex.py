from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

            triangle = []
            lastRow = triangle[-1] if triangle else []
            for i in range(1, rowIndex + 1):
                row = [1] * i;
                for j in range(1, len(lastRow)):
                    row[i] = lastRow[j - 1] + lastRow[j]
                    triangle.append(row);
            return triangle[-1] if triangle else []


if __name__ == "__main__":
    print("Hi There!!")
    l1 = Solution()
    print(l1.generate(3))
