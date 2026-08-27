class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        ans=0
        for num in s:
            if num-1 not in s:
                curr=1
                while num+curr in s:
                    curr+=1
                ans=max(ans,curr)
        return ans

        