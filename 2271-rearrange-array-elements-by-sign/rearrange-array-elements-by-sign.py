class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if nums is None:
            return
        ans = [0] * len(nums)
        p, n = 0, 1

        for num in nums:
            if num > 0:
                ans[p] = num
                p += 2
            else:
                ans[n] = num
                n += 2

        return ans