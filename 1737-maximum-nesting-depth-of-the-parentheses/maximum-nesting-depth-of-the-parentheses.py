class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
                if count > ans:
                    ans = count
            elif s[i] == ")":
                count -= 1
        return ans