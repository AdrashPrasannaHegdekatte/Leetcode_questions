class Solution(object):
    def solve(self, board):
        from collections import defaultdict
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!="O":
                return
            board[i][j]="A"
            for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(i+dx,j+dy)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    if(i==m-1 or i==0) or (j==n-1 or j==0):
                        dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j]=="A":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"
        
        
        