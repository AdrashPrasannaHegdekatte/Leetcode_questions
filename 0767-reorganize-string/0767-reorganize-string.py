class Solution(object):
    def reorganizeString(self, s):
        from collections import Counter
        import heapq
        """
        :type s: str
        :rtype: str
        """
        freq=Counter(s)
        ans=""
        heap=[]
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        prev=None
        while heap:
            val,key=heapq.heappop(heap)
            if prev==key:
                if not heap:
                    return ""
                nval,nkey=heapq.heappop(heap)
                nval+=1
                ans+=nkey
                prev=nkey
                if nval<0:
                    heapq.heappush(heap,(nval,nkey))
                heapq.heappush(heap,(val,key))

            else:
                val+=1
                ans+=key
                prev=key
                if val<0: heapq.heappush(heap,(val,key))
           
        return ans
        
                

        
        