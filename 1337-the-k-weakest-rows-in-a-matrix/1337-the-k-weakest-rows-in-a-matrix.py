class Solution(object):
    def kWeakestRows(self, mat, k):
        import heapq
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        heap=[]
        for i,row in enumerate(mat):
            l=0
            h=len(row)
            while(l<h):
                mid=l+(h-l)//2
                if row[mid]==0:
                    h=mid
                else:
                    l=mid+1
            heapq.heappush(heap,(l,i))
        while k:
            key,idx=heapq.heappop(heap)
            ans.append(idx)
            k-=1
        return ans