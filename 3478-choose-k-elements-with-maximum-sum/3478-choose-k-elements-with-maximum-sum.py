class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums1)
        ans=[0]*n
        indexed=list(enumerate(nums1))
        indexed.sort(key=lambda x:x[1])
        heap=[]
        curr_sum=0
        i=0

        while i<n:
            j=i
            while j<n and indexed[j][1]==indexed[i][1]:
                j+=1

            for t in range(i,j):
                idx=indexed[t][0]
                ans[idx]=curr_sum

            for t in range(i,j):
                idx=indexed[t][0]
                x=nums2[idx]

                if len(heap)<k:
                    curr_sum+=x
                    heapq.heappush(heap,x)
                elif x>heap[0]:
                    curr_sum+=x-heap[0]
                    heapq.heapreplace(heap,x)
            i=j
        return ans




        