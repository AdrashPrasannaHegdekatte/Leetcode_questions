class Solution(object):
    def maximumProduct(self, nums, k):
        import heapq
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        heapq.heapify(nums)

        for _ in range(k):
            if nums:
                val=heapq.heappop(nums)
                heapq.heappush(nums,val+1)
        ans=1
        MOD=10**9+7
        while nums:
            ans=(ans*heapq.heappop(nums))%MOD
        return ans