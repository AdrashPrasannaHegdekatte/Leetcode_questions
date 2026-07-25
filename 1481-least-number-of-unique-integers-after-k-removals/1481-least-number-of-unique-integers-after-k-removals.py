class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        from collections import Counter
        import heapq
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq=Counter(arr)
        heap=[]
        n=len(freq)

        heap=list(freq.values())
        heapq.heapify(heap)
        

        while heap and k>=heap[0]:
            k-=heap[0]
            heapq.heappop(heap)
            n-=1
        return n
