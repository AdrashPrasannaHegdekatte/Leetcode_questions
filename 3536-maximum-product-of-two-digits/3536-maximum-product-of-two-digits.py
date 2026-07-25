class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=-1
        sec_max=-1

        while n:
            rem=n%10
            if rem>m:
                sec_max=m
                m=rem
                n=n//10
                continue
            if rem>sec_max:sec_max=rem
            n=n//10
        return m*sec_max
        