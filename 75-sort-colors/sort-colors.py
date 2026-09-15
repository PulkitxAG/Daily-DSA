class Solution:
        def sortColors(self, nums: List[int]) -> None:
            # nums[:]=[0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)
            count_0 = nums.count(0)
            count_1 = nums.count(1)
            count_2 = nums.count(2)
            i = 0
            while (count_0):
                nums[i] = 0
                i += 1
                count_0 -=1
            while (count_1):
                nums[i] = 1
                i += 1
                count_1 -= 1
            while (count_2):
                nums[i] = 2
                i += 1
                count_2 -= 1