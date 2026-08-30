class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=2:return n
        maxElem=nums[0]
        minElem=nums[0]
        maxind,minind=0,0
        for i in range(n):
            if nums[i]>maxElem:
                maxElem=nums[i]
                maxind=i
            if nums[i]<minElem:
                minElem=nums[i]
                minind=i
        f=min(maxind,minind)
        l=max(maxind,minind)
        return min(l+1,n-f,(f+n-l+1))

        