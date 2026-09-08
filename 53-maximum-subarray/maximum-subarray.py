class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        # current_sum = nums[0]

        # max_sum = nums[0]

        # for i in range(1, len(nums)):

        #     current_sum = max(nums[i], current_sum + nums[i])

        #     max_sum = max(max_sum, current_sum)

        # return max_sum

        sum = 0
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            if sum + nums[i] > nums[i]:
                sum = sum + nums[i]
            else:
                sum = nums[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum