class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n+1):
            ans^=i
        for x in nums:
            ans^=x
        return ans