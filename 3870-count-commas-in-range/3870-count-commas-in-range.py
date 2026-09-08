class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        diff=n-1000+1
        return diff if diff>0 else 0 

        