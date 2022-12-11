class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True

        elif num < 1:
            return False

        flag = False

        while not flag:

            if num % 2 == 0:
                num //= 2

            elif num % 3 == 0:
                num //= 3

            elif num % 5 == 0:
                num //= 5

            elif num == 1:
                return True

            else:
                return False


S = Solution()
S.isUgly(12)
