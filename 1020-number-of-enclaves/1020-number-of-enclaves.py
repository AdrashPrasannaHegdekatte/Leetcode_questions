class Solution(object):
    def numEnclaves(self, grid):
        from collections import deque
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        cnt=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if (i==0 or j==0 or i==m-1 or j==n-1) and grid[i][j]==1:
                    q.append((i,j))
                    grid[i][j]=0
        while q:
            a,b=q.popleft()
            for x,y in d:
                nx=a+x
                ny=b+y
                if nx>=0 and ny>=0 and nx<m and ny<n and grid[nx][ny]==1:
                    q.append((nx,ny))
                    grid[nx][ny]=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:cnt+=1
        return cnt

        