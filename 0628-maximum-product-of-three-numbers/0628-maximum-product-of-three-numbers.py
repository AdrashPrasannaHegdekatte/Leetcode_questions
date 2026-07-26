class Solution(object):
    def maximumProduct(self, nums):
        import heapq
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        heap = []      
        minHeap = []   
        for x in nums:
            if len(heap) < 3:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)

            if len(minHeap) < 2:
                heapq.heappush(minHeap, -x)
            elif x < -minHeap[0]:
                heapq.heapreplace(minHeap, -x)
        ans = 1
        for x in heap:
            ans *= x
        smallest = sorted([-x for x in minHeap])
        ans = max(ans, smallest[0] * smallest[1] * max(heap))

        return ans