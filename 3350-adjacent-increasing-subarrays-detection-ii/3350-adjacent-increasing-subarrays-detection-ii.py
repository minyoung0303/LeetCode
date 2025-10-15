class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1
        
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = dec[i + 1] + 1

        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(inc[i], dec[i + 1]))
        return ans
