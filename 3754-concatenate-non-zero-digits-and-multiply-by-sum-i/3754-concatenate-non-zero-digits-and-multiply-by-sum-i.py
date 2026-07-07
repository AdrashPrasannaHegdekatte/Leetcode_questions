class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=0
        x=""
        s=str(n)
        for char in s:
            if char!='0':
                x+=char
                t+=int(char)
        return int(x)*t if n else 0
        