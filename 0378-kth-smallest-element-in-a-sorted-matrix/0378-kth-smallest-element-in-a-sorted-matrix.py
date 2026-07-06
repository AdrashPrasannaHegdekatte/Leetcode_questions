class Solution(object):
    def kthSmallest(self, matrix, k):
        import heapq
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap=[]
        c=0
        for i in range(len(matrix)):
            heapq.heappush(heap,(matrix[i][0],(i,0)))
        while(c<k):
            if heap:
                val,(row,col)=heapq.heappop(heap)
                if col+1<len(matrix):
                    heapq.heappush(heap,(matrix[row][col+1],(row,col+1)))
                c+=1
            else:
                break
        return val
                
            

        