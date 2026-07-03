class Solution(object):
    def findRightInterval(self, intervals):
        import heapq
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n=len(intervals)
        ans=[-1]*n
        sh=[]
        eh=[]

        for i,(st,end) in  enumerate(intervals):
            heapq.heappush(sh,(-st,i))
            heapq.heappush(eh,(-end,i))
        while eh:
            negEnd,endidx=heapq.heappop(eh)
            end=-negEnd

            if sh and -sh[0][0]>=end:
                c=heapq.heappop(sh)
                while sh and -sh[0][0]>=end:
                    c=heapq.heappop(sh)
                ans[endidx]=c[1]
                heapq.heappush(sh,c)
        return ans


                


        