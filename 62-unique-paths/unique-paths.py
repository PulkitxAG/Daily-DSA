class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        down = m - 1
        result = 1
        for i in range(1, down + 1):
            result = result * (total - i + 1) // i
        return result