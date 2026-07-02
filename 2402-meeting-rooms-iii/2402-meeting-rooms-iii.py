class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        import heapq
        meetings.sort()
        avail=list(range(n))
        heapq.heapify(avail)
        occupied=[]
        count=[0]*n

        for st,end in meetings:
            while occupied and occupied[0][0]<=st:
                et,rmn=heapq.heappop(occupied)
                heapq.heappush(avail,rmn)
            if avail:
                room=heapq.heappop(avail)
                heapq.heappush(occupied,(end,room))
            else:
                end_time,room=heapq.heappop(occupied)
                d=end-st
                new_end=d+end_time
                heapq.heappush(occupied,(new_end,room))
            count[room]+=1
        m=0
        idx=0
        for i in range(len(count)):
            if m<count[i]:
                m=count[i]
                idx=i
        return idx



         
        