class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        m,n=len(arr1),len(arr2)
        cnt=m
        for i in range(m):
            found=False
            for j in range(n):
                if abs(arr1[i]-arr2[j])<=d:
                    cnt-=1
                    break

        return cnt
        