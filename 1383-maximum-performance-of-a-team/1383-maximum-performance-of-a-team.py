class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        import heapq
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD=10**9+7
        heap=[]

        l=sorted(zip(speed,efficiency),reverse=True,key=lambda x:x[1])

        curr_sum=0
        pf=0

        for sp,eff in l:
            if len(heap)<k:
                heapq.heappush(heap,sp)
                curr_sum+=sp
                
            elif heap[0]<sp:
                curr_sum=curr_sum-heap[0]+sp
                heapq.heapreplace(heap,sp)

            pf=max(pf,curr_sum*eff)

        return pf%MOD
