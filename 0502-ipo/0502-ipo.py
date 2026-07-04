class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        import heapq
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        project=list(zip(capital,profits))
        project.sort()
        heap=[]
        i=0
        while k:
            while i<len(project) and project[i][0]<=w:
                heapq.heappush(heap,-project[i][1])
                i+=1
            if not heap:
                break
            w-=heapq.heappop(heap)
            k-=1
        return w


        