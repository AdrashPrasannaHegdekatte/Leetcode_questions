class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter,deque
        import heapq
        freq=Counter(tasks)
        heap=[]
        for f in freq.values():
            heap.append(-f)
        heapq.heapify(heap)
        rem=deque()
        time=0    
        while heap or rem:
            time+=1
            while rem and rem[0][0]<=time:
                _,cnt=rem.popleft()
                heapq.heappush(heap,cnt)
            if heap:
                cnt=heapq.heappop(heap)
                cnt+=1
                if cnt!=0:
                    rem.append((time+n+1,cnt))
        return time


