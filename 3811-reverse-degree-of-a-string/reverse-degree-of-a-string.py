class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ans = 0
        for i in range(len(s)):
            value = alphabet.index(s[i]) + 1
            reverse_value = 26 - value + 1
            ans += reverse_value * (i + 1)
        return ans