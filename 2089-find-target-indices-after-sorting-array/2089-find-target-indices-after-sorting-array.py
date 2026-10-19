class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        n=len(nums)
        l=0
        ans=[]
        r=n-1
        while(l<r):
            mid=l+(r-l)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        while(l<n and nums[l]==target):
            ans.append(l)
            l+=1
        return ans
