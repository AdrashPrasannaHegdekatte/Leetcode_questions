class Solution(object):
    def minimumPushes(self, word):
        from collections import Counter
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        freq=[0]*26
        for w in word:
            freq[ord(w)-97]+=1
        freq.sort(reverse=True)
        c=0
        m=1
        cost=0
        for val in freq:
            if val==0:continue
            m=c//8+1
            cost=cost+val*m
            c+=1
        return cost

        