class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d={}
        for name,val in knowledge:
            d[name]=val
        n=len(s)
        i=0
        ans=""
        while i<n:
            if s[i]=="(":
                curr=""
                i+=1
                while s[i]!=")":
                    curr+=s[i]
                    i+=1
                   
                if curr in d:
                    ans+=d[curr]
                else:
                    ans+="?"
            else:
                ans+=s[i]
            i+=1
        return ans
        


        