class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        ans=0
        l=0
        cntz=0
        for r in range(n):
            if nums[r]==0:
                cntz+=1
            while (cntz>k):
                if nums[l]==0:
                    cntz-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
        