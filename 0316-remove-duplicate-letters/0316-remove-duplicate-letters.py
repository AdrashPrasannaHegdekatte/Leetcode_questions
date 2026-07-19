class Solution(object):
    def removeDuplicateLetters(self, s):
        from collections import Counter
        """
        :type s: str
        :rtype: str
        """
        freq=Counter(s)
        stack=[]
        seen=set()

        for c in s:
            freq[c]-=1
            if c not in seen:
                while stack and freq[stack[-1]]>0 and stack[-1]>c:
                    p=stack.pop()
                    seen.remove(p)
                stack.append(c)
                seen.add(c)
        return "".join(stack)


        