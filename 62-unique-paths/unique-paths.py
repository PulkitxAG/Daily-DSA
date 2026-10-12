class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # total = m + n - 2
        # down = m - 1
        # result = 1
        # for i in range(1, down + 1):
        #     result = result * (total - i + 1) // i
        # return result

        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
