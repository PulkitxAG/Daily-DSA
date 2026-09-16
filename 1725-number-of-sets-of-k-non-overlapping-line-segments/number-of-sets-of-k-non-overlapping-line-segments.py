class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        a = n + k - 1
        b = 2 * k

        ans = 1

        for i in range(1, b + 1):
            ans = ans * (a - i + 1)
            ans = ans // i

        return ans % MOD