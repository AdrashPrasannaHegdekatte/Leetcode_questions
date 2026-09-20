class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            ans+=(i+1)*(26-(ord(s[i])-97))

        return ans