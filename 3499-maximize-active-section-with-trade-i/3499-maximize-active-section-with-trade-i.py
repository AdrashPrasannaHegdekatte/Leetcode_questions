class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        z=[]
        best=0
        ones=0
        i=0

        while i<n:
            if s[i]=="0":
                j=i
                while j<n and s[j]==s[i]:j+=1
                z.append(j-i)
                i=j
            else:
                ones+=1
                i+=1

        for i in range(len(z)-1):
            best=max(best,z[i]+z[i+1])
        return best+ones