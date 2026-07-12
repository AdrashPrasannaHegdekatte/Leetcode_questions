class Solution(object):
    def arrayRankTransform(self, arr):
        import heapq
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(arr)
        heap=[]
        for i,num in  enumerate(arr):
            heapq.heappush(heap,(num,i))
        r=0
        prev=None
        while(heap):
            val,idx=heapq.heappop(heap)
            if prev==val:
                ans[idx]=r
            else:
                r=r+1
                ans[idx]=r
            prev=val
        return ans
            
        