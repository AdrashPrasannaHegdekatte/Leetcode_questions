class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        import heapq
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr:
            return []
        n=len(arr)
        heap=[((arr[0]*1.0/arr[-1]),0,n-1)]
        c=0
        seen={(0,n-1)}
        while heap:
            f,i,j=heapq.heappop(heap)
            c+=1
            if c==k:
                return [arr[i],arr[j]]
            if i+1<j:
                ni=i+1
                if not (ni,j) in seen:
                    nf=arr[ni]*1.0/arr[j]
                    heapq.heappush(heap,(nf,ni,j))
                    seen.add((ni,j))
            if j-1>i:
                nj=j-1
                if not (i,nj) in seen:
                    nf=arr[i]*1.0/arr[nj]
                    heapq.heappush(heap,(nf,i,nj))
                    seen.add((i,nj))
            
    
        