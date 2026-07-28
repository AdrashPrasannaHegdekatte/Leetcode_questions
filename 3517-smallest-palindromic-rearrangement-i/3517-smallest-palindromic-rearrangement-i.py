class Solution(object):
    def smallestPalindrome(self, s):
        from collections import Counter
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n==1:return s
        ans=[""]*n
        freq=Counter(s)
        i,j=0,n-1
    
        for key in sorted(freq):
            while freq[key]>=2:
                ans[i]=key
                ans[j]=key
                i+=1
                j-=1
                freq[key]-=2
            if freq[key]==1:
                ans[n//2]=key
                freq[key]-=1
            
        return "".join(ans)   
       
            

        