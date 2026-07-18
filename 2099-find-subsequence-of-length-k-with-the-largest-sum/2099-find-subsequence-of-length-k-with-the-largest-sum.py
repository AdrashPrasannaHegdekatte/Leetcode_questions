class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq

        heap=[]
        n=len(nums)
    
        for i in range(k):
            heapq.heappush(heap,(nums[i],i))

        for i in range(k,n):
            if nums[i]>heap[0][0]:
                heapq.heapreplace(heap,(nums[i],i))
        heap.sort(key=lambda x:x[1])
        return [num for num,idx in heap]