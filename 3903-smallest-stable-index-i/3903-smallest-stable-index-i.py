class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            if max(nums[:i+1]) - min(nums[i:])<=k:
                return i
        return -1
        