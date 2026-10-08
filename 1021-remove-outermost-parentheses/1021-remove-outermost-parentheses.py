class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        d=0

        for ch in s:
            if ch=='(':
                if d>0:
                    ans.append(ch)
                d+=1
            else:
                d-=1
                if d>0:
                    ans.append(ch)
        return ''.join(ans)
        