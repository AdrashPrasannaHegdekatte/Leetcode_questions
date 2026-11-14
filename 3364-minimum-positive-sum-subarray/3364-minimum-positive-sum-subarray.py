class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n=len(nums)
        ans=float("inf")
        for i in range(n):
            s=0
            for j in range(i,n):
                m=j-i+1
                s+=nums[j]
                if l<=m<=r and s>0:
                    ans = min(ans, s)
        return -1 if ans==float("inf") else ans

