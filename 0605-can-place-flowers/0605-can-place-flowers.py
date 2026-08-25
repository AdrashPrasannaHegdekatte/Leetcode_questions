class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        m=len(flowerbed)
        for i in range(m):
            if i==0:
                if flowerbed[i]==0 and (m==1 or flowerbed[i+1]==0):
                    flowerbed[i]=1
                    n-=1
            elif i==m-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    n-=1
            elif flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]== 0:
                flowerbed[i]=1
                n-=1
            if n==0:
                return True
        return False
        