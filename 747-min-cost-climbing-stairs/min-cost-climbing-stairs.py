class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = 0
        n = len(cost)
        if n == 0:
            return 0
        for i in range(2,n+1):
            x = b + cost[i-1]
            y = a + cost[i-2]
            if x < y:
                c = x
            else:
                c = y
            a = b
            b = c
        return b
