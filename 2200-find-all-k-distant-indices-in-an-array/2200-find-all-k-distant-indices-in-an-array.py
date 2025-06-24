class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        result = set()
        for i, val in enumerate(nums):
            if val == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    result.add(j)
        return sorted(result)