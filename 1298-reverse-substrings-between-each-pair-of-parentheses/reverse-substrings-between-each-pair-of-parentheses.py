class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                for x in temp:
                    stack.append(x)
            else:
                stack.append(ch)
        return ''.join(stack)