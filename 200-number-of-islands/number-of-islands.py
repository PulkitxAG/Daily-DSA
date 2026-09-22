from collections import deque
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count = 0
        directions = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    q = deque()
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            new_row = row + dr
                            new_col = col + dc
                            if (0 <= new_row < m and
                                0 <= new_col < n and
                                grid[new_row][new_col] == '1' and
                                (new_row, new_col) not in visited):
                                visited.add((new_row, new_col))
                                q.append((new_row, new_col))
        return count