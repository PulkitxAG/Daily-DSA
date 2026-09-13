class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        for x in range(-n + 1, n):
            for y in range(-n + 1, n):
                count = 0
                for i in range(n):
                    for j in range(n):
                        ni = i + x
                        nj = j + y
                        if ni >= 0 and ni < n and nj >= 0 and nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                count += 1
                if count > ans:
                    ans = count
        return ans