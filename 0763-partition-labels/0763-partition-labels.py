class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans=[]
        n=len(s)
        last={}
        for i in range(n):
            last[s[i]]=i
        
        end,start=0,0
        for i in range(n):
            end=max(end,last[s[i]])
            if i==end:
                ans.append(end-start+1)
                start=end+1
        return ans