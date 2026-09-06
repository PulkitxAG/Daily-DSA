class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        arr = [0, 1, 1]
        for i in range(3, n + 1):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        return arr[n]