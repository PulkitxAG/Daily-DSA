class Solution:
    def climbStairs(self, n):
        step1 = 1
        step2 = 0
        for i in range(1, n+1):
            cur = step1 + step2
            step2 = step1
            step1 = cur
        return step1