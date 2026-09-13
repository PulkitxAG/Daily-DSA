from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    q = deque()
                    q.append((i, j))
                    visited[i][j] = 1
                    while q:
                        r, c = q.popleft()
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
                                grid[nr][nc] == "1" and
                                visited[nr][nc] == 0):
                                visited[nr][nc] = 1
                                q.append((nr, nc))
        return count