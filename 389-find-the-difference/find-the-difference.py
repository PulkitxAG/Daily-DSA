class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i in s:
            ans = ans ^ ord(i)
        for j in t:
            ans = ans ^ ord(j)
        return chr(ans)