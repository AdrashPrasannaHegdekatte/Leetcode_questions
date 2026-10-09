class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d=0
        res=0
        for char in s:
            if char=="(":
                d+=2
                if d%2==1:
                    res+=1
                    d-=1
            else:
                d-=1
                if d<0:
                    res+=1
                    d=1
        return res+d