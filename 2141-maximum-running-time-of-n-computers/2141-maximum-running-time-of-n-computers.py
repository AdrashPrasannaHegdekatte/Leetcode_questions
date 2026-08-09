class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        def helper(val):
            s=0
            for bat in batteries:
                s+=min(val,bat)
            return s>=n*val
        l,r=0,sum(batteries)//n+1

        while(l<r):
            mid=l+(r-l)//2

            if helper(mid):
                l=mid+1
            else:
                r=mid
        return l-1
        