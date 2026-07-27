# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        h=n

        while(l<=h):
            mid=l+(h-l)//2
            if isBadVersion(mid):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
        