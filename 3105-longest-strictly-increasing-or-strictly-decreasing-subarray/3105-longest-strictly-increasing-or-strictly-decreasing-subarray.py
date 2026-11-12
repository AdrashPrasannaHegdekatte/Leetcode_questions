class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt1,cnt2=1,1
        n=len(nums)
        l=0
        for r in range(1,n):
            if not nums[r-1]<nums[r]:
                l=r
            cnt1=max(cnt1,r-l+1)
        l=0
        for r in range(1,n):
            if not nums[r-1]>nums[r]:
                l=r
            cnt2=max(cnt2,r-l+1)
        return max(cnt1,cnt2)