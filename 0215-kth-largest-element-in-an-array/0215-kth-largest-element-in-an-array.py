class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        heap=[]

        for i in range(k):
            heapq.heappush(heap,nums[i])

        for i in range(k,n):
            if nums[i]>heap[0]:
                heapq.heappush(heap,nums[i])
                heapq.heappop(heap)
        return heap[0]
            
            


    