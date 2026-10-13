class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        i=0
        j=n-1
        s=0
        while(i<j):
           s+=(nums[j]-nums[i])
           i+=1
           j-=1
        if n%2==1:s+=nums[i]
        return s 
        