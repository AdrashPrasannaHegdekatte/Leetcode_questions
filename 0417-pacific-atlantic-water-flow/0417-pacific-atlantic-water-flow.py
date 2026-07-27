class Solution(object):
    def pacificAtlantic(self, heights):
        from collections import deque
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n=len(heights),len(heights[0])

        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        p=deque()
        a=deque()

        for i in range(m):
            p.append((i,0))
        for j in range(n):
            p.append((0,j))
        for i in range(m):
            a.append((i,n-1))
        for j in range(n):
            a.append((m-1,j))
        def bfs(q):
            visited=set(q)
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    nr=dr+r
                    nc=c+dc
                    if(0<=nc<n and 0<=nr<m and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return visited
        pac=bfs(p)
        atl=bfs(a)

        ans=[]

        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])
        return ans
        
        