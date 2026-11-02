class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        elem=nums[n//2] if n%2==1 else (nums[n//2]+nums[n//2-1])//2

        cnt=0
        for num in nums:
            cnt+=(abs(num-elem))
        return cnt