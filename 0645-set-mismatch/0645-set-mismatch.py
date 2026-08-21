class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        i=0

        while i<n:
            j=nums[i]-1
            if nums[i]!=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1 

        for k in range(n):
            if nums[k]!=k+1:
                return [nums[k],k+1]