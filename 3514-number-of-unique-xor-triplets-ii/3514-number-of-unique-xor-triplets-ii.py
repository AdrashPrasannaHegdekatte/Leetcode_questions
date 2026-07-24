class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        seen=set()
        add_seen=seen.add
        for i in range(n):
            for j in range(i,n):
                add_seen(nums[i]^nums[j])

        res=set()
        res_seen=res.add
        for i in range(n):
            a=nums[i]
            for val in seen:
                res_seen(a^val)
        return len(res)