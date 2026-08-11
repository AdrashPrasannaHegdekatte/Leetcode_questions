class Solution(object):
    def nearestExit(self, maze, entrance):
        from collections import deque
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m,n=len(maze),len(maze[0])
        q=deque([(entrance[0],entrance[1],0)])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        vis={(entrance[0],entrance[1])}
        
        while q:
            i,j,step=q.popleft()
            if (i,j)!=(entrance[0],entrance[1]):
                if i==0 or i==m-1 or j==0 or j==n-1:return step
            for dx,dy in directions:
                nr=dx+i
                nc=dy+j
                
                if 0<=nc<n and 0<=nr<m and (nr,nc) not in vis and maze[nr][nc]=='.':
                    vis.add((nr,nc))
                    q.append((nr,nc,step+1))
        return -1
        