class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        firstRow=False
        firstCol=False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i==0: firstRow=True
                    if j==0: firstCol=True
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1 , m):
            for j in range(1 , n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if(firstRow):
            for j in range(n):
                matrix[0][j]=0
        if(firstCol):
            for i in range(m):
                matrix[i][0]=0
        

        
                
        