class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return max((nums[-1]-1)*(nums[-2]-1),(nums[0]-1)*(nums[1]-1))
        