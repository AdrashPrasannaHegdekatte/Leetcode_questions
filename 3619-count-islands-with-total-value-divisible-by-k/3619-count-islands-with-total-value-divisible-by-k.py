class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        from collections import deque
        m,n=len(grid),len(grid[0])
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    q=deque([(i,j)])
                    s=grid[i][j]
                    grid[i][j]=0
                    while q:
                        r,c=q.popleft()
                        for dr,dc in dir:
                            nr=r+dr
                            nc=c+dc

                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]!=0:
                                s+=grid[nr][nc]
                                grid[nr][nc]=0
                                q.append((nr, nc))
    
                    if s%k==0:
                        cnt+=1
        return cnt

        
        