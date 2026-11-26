class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt=10
        ans=0
        while(cnt>0 and n>=cnt):
            n-=cnt
            cnt-=1
            ans+=1
        return ans%2==1
        