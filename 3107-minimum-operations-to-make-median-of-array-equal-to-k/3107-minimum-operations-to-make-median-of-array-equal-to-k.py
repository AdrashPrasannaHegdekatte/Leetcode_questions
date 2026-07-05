class Solution(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        c=0
        n=len(nums)
        idx=n//2
        if k==nums[idx]:
            return c
        elif k<nums[idx]:
            for i in range(idx+1):
                if nums[i]>k:
                    c+=nums[i]-k
        else:
            for i in range(idx,n):
                if nums[i]<k:
                    c+=k-nums[i]
        return c

            