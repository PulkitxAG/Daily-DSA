class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)

        # pal[j] tells whether s[j...i] is palindrome
        pal = [False] * n

        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)

        for i in range(n):

            dp[i + 1] = dp[i]

            for j in range(i + 1):

                if s[j] == s[i]:

                    if i - j <= 1:
                        pal[j] = True
                    else:
                        pal[j] = pal[j + 1]

                else:
                    pal[j] = False

                if pal[j] and i - j + 1 >= k:
                    if dp[j] + 1 > dp[i + 1]:
                        dp[i + 1] = dp[j] + 1

        return dp[n]