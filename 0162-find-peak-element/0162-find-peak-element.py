class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        h=len(nums)-1

        while(l<h):
            mid=l+(h-l)//2

            if nums[mid]>nums[mid+1]:
                h=mid
            else:
                l=mid+1
        return l
        