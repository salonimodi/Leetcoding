class Solution:
    def isValid(self, s: str) -> bool:
        q = [0]
        for bracket in s:
            if bracket == '}' and q[-1] == '{':
                q.pop()
            elif bracket == ']' and q[-1] == '[':
                q.pop()
            elif bracket == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(bracket)
        if len(q) > 1:
            return False
        else:
            return True


s = Solution()
print(s.isValid("(])"))
