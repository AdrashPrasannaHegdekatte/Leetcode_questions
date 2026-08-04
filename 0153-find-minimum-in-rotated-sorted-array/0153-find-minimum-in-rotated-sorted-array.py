class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l,r=0,n-1

        while(l<r):
            mid=l +(r-l)//2
            if nums[r]<nums[mid]:
                l=mid+1
            else:
                r=mid
        return nums[l]
        