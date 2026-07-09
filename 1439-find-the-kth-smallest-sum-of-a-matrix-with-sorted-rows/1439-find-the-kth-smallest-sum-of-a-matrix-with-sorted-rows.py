class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        m=len(mat)
        n=len(mat[0])
        s=sum(mat[i][0] for i in range(m))
        heap=[]
        c=0
        idxs=tuple([0]*m)
        heapq.heappush(heap,(s,idxs))
        seen={idxs}
        while heap and c<k:
            old_s,l=heapq.heappop(heap)
            c+=1
            for row in range(m):
                if l[row]+1<n:
                    nl=list(l)
                    nl[row]+=1
                    nl=tuple(nl)

                if nl not in seen:
                    seen.add(nl)
                    n_s=old_s-mat[row][l[row]]+mat[row][nl[row]]
                    heapq.heappush(heap,(n_s,nl))
                    
        return old_s

                
                

                
