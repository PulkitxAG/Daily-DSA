class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        def dfs(r, c):
            image[r][c] = color
            if r - 1 >= 0 and image[r - 1][c] == old:
                dfs(r - 1, c)
            if r + 1 < len(image) and image[r + 1][c] == old:
                dfs(r + 1, c)
            if c - 1 >= 0 and image[r][c - 1] == old:
                dfs(r, c - 1)
            if c + 1 < len(image[0]) and image[r][c + 1] == old:
                dfs(r, c + 1)
        dfs(sr, sc)
        return image