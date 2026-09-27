from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = 1
        max_distance = 0
        while q:
            r, c, distance = q.popleft()
            max_distance = max(max_distance, distance)
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    grid[nr][nc] == 1 and
                    visited[nr][nc] == 0):
                    visited[nr][nc] = 1
                    q.append((nr, nc, distance + 1))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    return -1
        return max_distance