class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = bin(n)[2:].zfill(32)
        rev_bin = bin_str[::-1]
        return int(rev_bin, 2)