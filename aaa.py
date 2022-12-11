import string


class Solution:
    def breakPalindrome(self, palindromeStr):
        # Write your code here
        ans = "IMPOSSIBLE"
        n = len(palindromeStr)
        for i in range(n // 2):
            if (ans != "IMPOSSIBLE"):
                break;
            for alpha in string.ascii_lowercase:
                if palindromeStr[n - i - 1] != alpha and alpha < palindromeStr[i]:
                    ans = palindromeStr[:i] + alpha + palindromeStr[i + 1:]
                    break;
        for i in range(n // 2):
            if (ans != "IMPOSSIBLE"):
                break
            for alpha in string.ascii_lowercase:
                if palindromeStr[n - i - 1] != alpha and alpha < palindromeStr[i]:
                    ans = palindromeStr[:i] + alpha + palindromeStr[i + 1:]
                    break
        return ans


if __name__ == "__main__":
    print("Hi There!!")
    l1 = Solution()
    print(l1.breakPalindrome("aaa"))
