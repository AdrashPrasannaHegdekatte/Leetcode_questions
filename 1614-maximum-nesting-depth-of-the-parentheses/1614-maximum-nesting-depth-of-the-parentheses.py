class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        curr=0
        for char in s:
            if char==")":
                ans=max(ans,curr)
                curr-=1
            elif char=="(":
                curr+=1
        return ans
        