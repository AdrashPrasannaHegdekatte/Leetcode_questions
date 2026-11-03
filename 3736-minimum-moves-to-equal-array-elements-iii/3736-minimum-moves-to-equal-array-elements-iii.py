class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        cnt=0
        for num in nums:
            cnt+=m-num
        return cnt