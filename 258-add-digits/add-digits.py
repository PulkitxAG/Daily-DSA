class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            total=0
            for i in str(num):
                total+=int(i)
            num = total
        return num