class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        i=0
        j=n-1
        ans=0
        while(i<j):
            area=(j-i)*min(height[i],height[j])
            ans=max(area,ans)
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return ans        