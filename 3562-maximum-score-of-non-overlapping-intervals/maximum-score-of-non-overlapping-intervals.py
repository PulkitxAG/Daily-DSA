class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        a = []
        for i in range(n):
            a.append((intervals[i][0], intervals[i][1], intervals[i][2], i))
        a.sort()
        starts = [x[0] for x in a]
        nxt = [n] * n
        for i in range(n):
            l = i + 1
            r = n - 1
            while l <= r:
                m = (l + r) // 2
                if starts[m] > a[i][1]:
                    nxt[i] = m
                    r = m - 1
                else:
                    l = m + 1
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                x = dp[i + 1][k]
                j = nxt[i]
                if j < n:
                    y = (a[i][2] + dp[j][k - 1][0], dp[j][k - 1][1] + [a[i][3]])
                else:
                    y = (a[i][2], [a[i][3]])
                if y[0] > x[0] or (y[0] == x[0] and sorted(y[1]) < sorted(x[1])):
                    dp[i][k] = y
                else:
                    dp[i][k] = x
        return sorted(dp[0][4][1])