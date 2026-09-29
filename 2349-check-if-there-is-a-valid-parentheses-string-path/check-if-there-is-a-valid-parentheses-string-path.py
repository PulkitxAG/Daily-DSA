class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j,count):
            if grid[i][j]=="(":
                count+=1
            else:
                count-=1
            if count<0:
                return False
            if i==m-1 and j==n-1:
                return count==0
            if (i,j,count) in visited:
                return False
            visited.add((i,j,count))
            if i+1<m and dfs(i+1,j,count):
                return True
            if j+1<n and dfs(i,j+1,count):
                return True
            return False
        if grid[0][0]==")" or grid[m-1][n-1]=="(":
            return False
        return dfs(0,0,0)