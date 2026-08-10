# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        from collections import deque
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return None
        q=deque([root])
        leftMost=root.val
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                if i==0:leftMost=curr.val
                if curr.left:q.append(curr.left)
                if curr.right:q.append(curr.right)
        return leftMost