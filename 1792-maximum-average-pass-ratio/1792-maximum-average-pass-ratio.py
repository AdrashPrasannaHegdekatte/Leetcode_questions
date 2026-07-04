class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        import heapq
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        heap=[]
        for p,t in classes:
            gain=(t-p)/(t*(t+1.0))
            heapq.heappush(heap,(-gain,p,t))
        for _ in range(extraStudents):
            gain,p,t=heapq.heappop(heap)
            p+=1
            t+=1
            gain=(t-p)/(t*(t+1.0))
            heapq.heappush(heap,(-gain,p,t))
        total_sum=0.0
        while heap:
            _,passed,total=heapq.heappop(heap)
            total_sum+=passed/float(total)
        return total_sum/len(classes)

        