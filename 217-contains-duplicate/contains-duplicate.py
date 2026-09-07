class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in range(len(nums)):
            if nums[i] in temp:
                return True
            temp.add(nums[i])
        return False

