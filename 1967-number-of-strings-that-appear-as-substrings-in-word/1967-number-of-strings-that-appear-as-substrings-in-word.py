class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        cnt=0
        for w in patterns:
            if w in word:
                cnt+=1
        return cnt
        