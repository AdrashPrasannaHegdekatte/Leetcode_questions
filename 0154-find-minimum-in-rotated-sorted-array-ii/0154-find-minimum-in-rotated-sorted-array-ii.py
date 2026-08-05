class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l,r=0,len(nums)-1

        while(l<r):
            mid=l+(r-l)//2
            if nums[mid]==nums[l]==nums[r]:
                l+=1
                r-=1
            elif nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[l]:
                r=mid
            else:
                return nums[l]
        return nums[r]
        