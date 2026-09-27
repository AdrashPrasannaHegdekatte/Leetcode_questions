class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for char in s:
            if char==")":
                curr=[]
                while stack and stack[-1]!='(':
                    curr.append(stack.pop())
                stack.pop()
                stack+=curr
            else:
                stack.append(char)
        return "".join(stack)

        