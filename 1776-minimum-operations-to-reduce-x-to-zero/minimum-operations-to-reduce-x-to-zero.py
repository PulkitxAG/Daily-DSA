class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        start = 0
        total = 0
        longest = -1

        for end in range(len(nums)):
            total += nums[end]

            while total > target and start <= end:
                total -= nums[start]
                start += 1

            if total == target:
                longest = max(longest, end - start + 1)

        if longest == -1:
            return -1

        return len(nums) - longest