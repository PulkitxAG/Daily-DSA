class Solution:
    def climbStairs(self, n):
        # step1 = 1
        # step2 = 0
        # for i in range(1, n+1):
        #     cur = step1 + step2
        #     step2 = step1
        #     step1 = cur
        # return step1

        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[i]