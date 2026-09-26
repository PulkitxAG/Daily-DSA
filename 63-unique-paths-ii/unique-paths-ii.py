class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = {}
        def solve(i, j):
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in ans:
                return ans[(i, j)]
            ans[(i, j)] = solve(i + 1, j) + solve(i, j + 1)
            return ans[(i, j)]
        return solve(0, 0)