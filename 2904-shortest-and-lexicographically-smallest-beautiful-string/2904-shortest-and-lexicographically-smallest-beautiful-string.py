class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        ans=""
        l=0
        cnt=0
        for r in range(n):
            if s[r]=="1":
                cnt+=1
                while l<r and cnt>k:
                    if s[l]=="1":
                        cnt-=1
                    l+=1
                
                if cnt==k:
                    while l<r and s[l]=="0":
                        l+=1
                    size=r-l+1
                    if ans=="" or size<len(ans):
                        ans=s[l:r+1]
                    elif size==len(ans):
                        ans=min(s[l:r+1],ans)
        return ans

        