class Solution(object):
    def maxKelements(self, nums, k):
        import math,heapq
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        score=0

        heap=[]

        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])

        while heap and k>0:
            val=-heapq.heappop(heap)
            score+=val
            nval=math.ceil((val)/3.0)
            heapq.heappush(heap,-nval)
            k-=1
        return int(score)