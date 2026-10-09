class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # a = 0
        # b = 0
        # n = len(cost)
        # if n == 0:
        #     return 0
        # for i in range(2,n+1):
        #     x = b + cost[i-1]
        #     y = a + cost[i-2]
        #     if x < y:
        #         c = x
        #     else:
        #         c = y
        #     a = b
        #     b = c
        # return b

        n = len(cost)
        dp = [0]*n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

        return min(dp[n-1],dp[n-2])