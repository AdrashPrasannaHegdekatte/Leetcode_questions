class Solution(object):
    def kthLargestNumber(self, nums, k):
        import heapq
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        n=len(nums)
        heap=[]
        if k>n:
            return ""
        for i in range(k):
            heapq.heappush(heap,int(nums[i]))
        
        for j in range(k,n):
            m=int(nums[j])
            if heap[0]>m:
                continue
            heapq.heapreplace(heap,m)
        return str(heap[0])


        

        