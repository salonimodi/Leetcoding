import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]
        stack = []
        res = 0
        operators = ["+", "-", "*", "/"]
        prev = None
        for op in tokens:
            if stack and op in operators:
                if prev is None:
                    prev = int(stack.pop())
                if stack:
                    a = int(stack.pop())
                if op == "+":
                    prev = a+prev
                elif op == "-":
                    prev = prev - a
                elif op == "*":
                    prev = a * prev
                elif op == "/":
                    prev = math.ceil(a/prev) if (a > 0) ^ (prev > 0) else math.floor(a/prev)
            if op not in operators:
                stack.append(op)
        print(prev)


s = Solution()
s.evalRPN(["4","3","-"])
