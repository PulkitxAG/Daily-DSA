class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [1000000] * n
        left = 0
        total = 0
        ans = 1000000
        shortest = 1000000
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            if total == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != 1000000:
                    value = best[left - 1] + length
                    if value < ans:
                        ans = value
                if length < shortest:
                    shortest = length
            if right == 0:
                best[right] = shortest
            else:
                best[right] = best[right - 1]
                if shortest < best[right]:
                    best[right] = shortest
        if ans == 1000000:
            return -1
        return ans