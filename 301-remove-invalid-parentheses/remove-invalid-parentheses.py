class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        queue = [s]
        visited = set()
        visited.add(s)
        ans = []
        while queue:
            current = queue.pop(0)
            if self.isValid(current):
                ans.append(current)
            if len(ans) > 0:
                continue
            for i in range(len(current)):
                if current[i] != '(' and current[i] != ')':
                    continue
                new = current[:i] + current[i + 1:]
                if new not in visited:
                    visited.add(new)
                    queue.append(new)
        return ans
    def isValid(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0