class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        so=n*n
        se=n*(n+1)

        while(se):
            so,se=se,so%se
        return so
        

        