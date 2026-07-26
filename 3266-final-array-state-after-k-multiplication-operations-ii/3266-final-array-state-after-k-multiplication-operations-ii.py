class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        import heapq
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        MOD=10**9 + 7
        if multiplier==1:return nums
        n=len(nums)
        heap=[(nums[i],i) for i in range(n)]
        heapq.heapify(heap)
        ans=[0]*n
        mx=max(nums)
        while k and heap[0][0]<mx:
            val,idx=heapq.heappop(heap)
            nval=val*multiplier
            heapq.heappush(heap,(nval,idx))
            k-=1
        mul=k//n
        extra=k%n
        c=pow(multiplier,mul,MOD)
        heap.sort()
        for i,(v,j) in enumerate(heap):
            v=(v*c)%MOD
            if i<extra:
                v=(v*multiplier)%MOD
            ans[j]=v
        return ans
        