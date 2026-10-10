class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = []
        n = len(nums1)
        for i in range(n):
            d = nums1[i] - nums2[i]
            if d < 0:
                d = -d
            diff.append(d)
        k = k1 + k2
        total = 0
        for i in range(n):
            total += diff[i]
        if total <= k:
            return 0
        left = 0
        right = 0
        for i in range(n):
            if diff[i] > right:
                right = diff[i]
        while left < right:
            mid = (left + right) // 2
            operations = 0
            for i in range(n):
                if diff[i] > mid:
                    operations += diff[i] - mid
            if operations > k:
                left = mid + 1
            else:
                right = mid
        ans = 0
        operations = 0
        for i in range(n):
            if diff[i] > left:
                operations += diff[i] - left
                diff[i] = left
        remaining = k - operations
        for i in range(n):
            if diff[i] == left and remaining > 0:
                diff[i] -= 1
                remaining -= 1
        for i in range(n):
            ans += diff[i] * diff[i]
        return ans