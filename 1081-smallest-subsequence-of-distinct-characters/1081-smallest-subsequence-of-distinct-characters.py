class Solution(object):
    def smallestSubsequence(self, s):
        from collections import Counter
        """
        :type s: str
        :rtype: str
        """
        freq=Counter(s)
        seen=set()
        stack=[]

        for c in s:
            freq[c]-=1
            if c not in seen:
                while stack and c<stack[-1] and freq[stack[-1]]>0:
                        p=stack.pop()
                        seen.remove(p)
                stack.append(c)
                seen.add(c)
        return "".join(stack)

        


        