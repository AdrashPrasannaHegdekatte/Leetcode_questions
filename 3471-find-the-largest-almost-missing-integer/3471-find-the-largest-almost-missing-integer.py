class Solution(object):
    def largestInteger(self, nums, k):
        from collections import Counter
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        key=Counter(nums)
        if k == len(nums):return max(nums)
        ans=-1
        if k==1:
            for num in nums:
                if key[num]==1:
                    ans=max(ans,num)
            return ans
        f=nums[0]
        l=nums[-1]
        if key[f]==1 and key[l]==1:return max(f,l)
        if key[f]>1:
            if key[l]==1:return l
            return -1
        return f
        