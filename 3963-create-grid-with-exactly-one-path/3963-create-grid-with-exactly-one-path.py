class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        s=""
        for i in range(m):
            s=""
            for j in range(n):
                if i==0:
                    s+="."
                elif j==n-1:
                    s+="."
                else:
                    s+="#"

            ans.append(s)
        return ans
        