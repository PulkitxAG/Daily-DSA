from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n=len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        if n==1:
            return 1
        queue=deque([(0, 0, 1)])
        grid[0][0]=1
        directions=[
            (-1, -1),(-1,0),(-1,1),
            (0,-1),        (0,1),
            (1,-1),(1,0),(1,1)
        ]
        while queue:
            row,col,length=queue.popleft()
            for d_row,d_col in directions:
                n_row,n_col=row+d_row,col+d_col
                if 0<=n_row<n and 0<=n_col<n and grid[n_row][n_col]==0:
                    if n_row==n-1 and n_col==n-1:
                        return length+1
                    grid[n_row][n_col]=1
                    queue.append((n_row, n_col, length+1))
        return -1