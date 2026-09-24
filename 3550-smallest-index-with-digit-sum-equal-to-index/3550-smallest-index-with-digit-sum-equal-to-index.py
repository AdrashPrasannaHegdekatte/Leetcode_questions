class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        def sod(num):
            s=0
            while num:
                rem=num%10
                s+=rem
                num=num/10
            return s

        for i in range(n):
            if sod(nums[i])==i:return i
        return -1