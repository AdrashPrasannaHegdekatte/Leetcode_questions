class Solution(object):
    def smallestRange(self, nums):
        import heapq
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ans=[0]*2
        heap=[]
        n=len(nums)
        curr_max=float("-inf")
        for i in range(n):
            val=nums[i][0]
            heapq.heappush(heap,(val,0,i))
            curr_max=max(curr_max,val)
        minr=float("inf")
        while heap:
            v,i,l=heapq.heappop(heap)
            r=curr_max-v
            if r<minr:
                minr=r
                ans[0],ans[1]=nums[l][i],curr_max
            if i+1<len(nums[l]):
                i+=1
                curr_max=max(curr_max,nums[l][i])
                heapq.heappush(heap,(nums[l][i],i,l))
            else:
                return ans

        
            


            
            
