class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        stack=[]
        ans=[0]*n

        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev=stack.pop()
                ans[prev]=i-prev
            stack.append(i)
        return ans
        