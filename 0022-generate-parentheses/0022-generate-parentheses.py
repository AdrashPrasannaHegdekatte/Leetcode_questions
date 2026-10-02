class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ans=[]
        sol=[]

        def backtrack(o,c):
            if len(sol)==2*n:
                ans.append("".join(sol))
                return

            if o<n:
                sol.append('(')
                backtrack(o+1,c)
                sol.pop()
            if o>c:
                sol.append(')')
                backtrack(o,c+1)
                sol.pop()
            
        backtrack(0,0)
        return ans
            
        