class Solution(object):
    def maximumLengthSubstring(self, s):
        from collections import defaultdict
        """
        :type s: str
        :rtype: int
        """
        freq=defaultdict(int)
        l=0
        ans=0
        for r in range(len(s)):
            freq[s[r]]+=1
            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans



        