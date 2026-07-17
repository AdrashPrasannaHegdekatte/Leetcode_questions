class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly=[1]
        heap=[]

        for i,p in enumerate(primes):
            heapq.heappush(heap,(p,i,0))

        while len(ugly)<n:
            val=heap[0][0]
            ugly.append(val)

            while heap and heap[0][0]==val:
                v,pi,ui=heapq.heappop(heap)
                ui+=1

                heapq.heappush(heap,(primes[pi]*ugly[ui],pi,ui))
        return ugly[-1]