class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        d=0
        res=[]

        for char in seq:
            if char=="(":
                res.append(d%2)
                d+=1
            else:
                d-=1
                res.append(d%2)
        return res
