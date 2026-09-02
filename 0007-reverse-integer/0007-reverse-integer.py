class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        found=0
        if x<0:
            found=1
            x=abs(x)
        while x!=0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if found==1:rev=-rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

            
            