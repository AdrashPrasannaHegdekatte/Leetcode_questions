class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=0
        prev=""
        res=0
        for c in s:
            if c=="(":d+=1
            else:
                d-=1
            if prev=="(" and c==")":res+=2**d
            prev=c
        return res
                