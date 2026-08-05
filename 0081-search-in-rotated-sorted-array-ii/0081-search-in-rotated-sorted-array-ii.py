class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n=len(nums)
        l,r=0,n-1

        while(l<r):
            mid=l+(r-l)//2
            if nums[mid]==target:
                return True
            if nums[l]==nums[r]==nums[mid]:
                l+=1
                r-=1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r=mid
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid
        return nums[l]==target
        