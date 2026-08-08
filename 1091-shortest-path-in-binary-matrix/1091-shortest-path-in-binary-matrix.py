class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        from collections import deque
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:return -1
        vis = {(0, 0)}
        q=deque([(0,0,1)])
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),
                        (0, 1),(1, -1),(1, 0),(1, 1)]
        while q:
            r,c,d=q.popleft()
            if r == n-1 and c == n-1:
                return d
            for dr,dc in directions:
                nr=dr+r
                nc=c+dc

                if 0<=nr<n and 0<=nc<n and (nr,nc) not in vis and grid[nr][nc]==0:
                    vis.add((nr,nc))
                    q.append((nr,nc,d+1))

        return -1