class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dp(l,r):
            if l==r:return nums[l]
            left=nums[l]-dp(l+1,r)
            right=nums[r]-dp(l,r-1)
            return max(left,right)
        n=len(nums)
        return dp(0,n-1)>=0