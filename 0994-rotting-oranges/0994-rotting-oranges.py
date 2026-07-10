class Solution(object):
    def orangesRotting(self, grid):
        from collections import deque,defaultdict
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        q=deque()
        directions=((0,1),(0,-1),(1,0),(-1,0))
        f=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    f+=1
        t=0
        while q and f:
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        f=f-1
                        q.append((nx,ny))
            t+=1 
        return t if f==0 else -1