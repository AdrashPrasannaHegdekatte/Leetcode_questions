class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m,n=len(grid),len(grid[0])
        
        while k:
            prev=grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    temp=grid[i][j]
                    grid[i][j]=prev
                    prev=temp

            k-=1
        return grid