class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s="123456789"
        ans=[]
        ll=len(str(low))
        hl=len(str(high))

        for size in range(ll,hl+1):
            for st in range(10-size):
                num=int(s[st:st+size])
                if low<=num<=high:
                    ans.append(num)
        return ans