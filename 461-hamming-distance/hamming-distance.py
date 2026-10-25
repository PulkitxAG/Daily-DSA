class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x^y
        count = 0
        while ans > 0:
            if ans & 1:
                count += 1
            ans = ans >> 1
        return count