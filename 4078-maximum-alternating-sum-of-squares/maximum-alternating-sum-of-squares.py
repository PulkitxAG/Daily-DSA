
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        ans = 0
        n = len(nums)

        for i in range(n // 2):
            ans -= nums[i] * nums[i]

        for i in range(n // 2, n):
            ans += nums[i] * nums[i]

        return ans
