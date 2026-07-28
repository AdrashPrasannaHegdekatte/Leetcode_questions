class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w=w
        self.n=len(self.w)
        self.prefix=[0]*len(w)
        self.prefix[0]=self.w[0]
        for i in range(1,self.n):
            self.prefix[i]=self.prefix[i-1] + self.w[i]

        

    def pickIndex(self):
        import random
        """
        :rtype: int
        """
        r=random.random()

        l,h=0,self.n-1

        tar=r*self.prefix[-1]
        while(l<h):
            mid=l+(h-l)//2
            if self.prefix[mid]==tar:
                return mid

            if self.prefix[mid]>tar:
                h=mid
            else:
                l=mid+1
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()