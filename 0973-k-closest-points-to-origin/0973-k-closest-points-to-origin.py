class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq

        n=len(points)

        heap=[]

        for i in range(k):
            x,y=points[i]
            dis=(x**2+y**2)**0.5
            heapq.heappush(heap,(-dis,x,y))

        for j in range(k,n):
            a,b=points[j]
            ndis=(a**2+b**2)**0.5
            if ndis<-heap[0][0]:
                heapq.heapreplace(heap,(-ndis,a,b))
        ans=[]
        while heap:
            _,m,n=heapq.heappop(heap)
            ans.append([m,n])
        return ans