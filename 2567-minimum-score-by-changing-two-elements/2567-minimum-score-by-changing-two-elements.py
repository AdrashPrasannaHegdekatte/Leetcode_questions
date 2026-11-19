class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 4:return 0
        nums.sort()
        a = nums[-1]-nums[2]   
        b = nums[-3]-nums[0]   
        c = nums[-2]-nums[1]   
        return min(a,b,c)