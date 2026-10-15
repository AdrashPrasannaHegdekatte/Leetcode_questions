class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=0
        seen=set()
        for i in range(n):
            c=0
            for j in range(i,n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    c+=1
                s+=c*c
            seen.clear()
        return s
