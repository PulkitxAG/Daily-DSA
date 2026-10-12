class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # ans = float('inf')
        # def dfs(i, j, total):
        #     nonlocal ans
        #     if i == m - 1 and j == n - 1:
        #         if total < ans:
        #             ans = total
        #         return
        #     if i < m - 1:
        #         dfs(i + 1, j, total + grid[i + 1][j])
        #     if j < n - 1:
        #         dfs(i, j + 1, total + grid[i][j + 1])
        # solve(0, 0, grid[0][0])
        # return ans

        
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]
