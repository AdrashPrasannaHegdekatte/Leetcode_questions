class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        while(True):
            prod=1
            k=n
            while(k):
                rem=k%10
                prod*=rem
                k=k//10
            if prod%t==0:return n
            n+=1