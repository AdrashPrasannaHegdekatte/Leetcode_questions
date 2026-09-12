class Solution(object):
    def maxTwoEvents(self, events):
        import heapq
        """
        :type events: List[List[int]]
        :rtype: int
        """
        heap=[]
        max_prev=0
        res=0
        events.sort()
        for l,r,val in events:
            while heap and l>heap[0][0]:
                max_prev=max(max_prev,heapq.heappop(heap)[1])
            heapq.heappush(heap,(r,val))
            res=max(res,max_prev+val)
        return res