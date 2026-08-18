# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        from collections import deque
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        ans=[]
        q=deque([root])
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                if i==n-1:ans.append(node.val)
        return ans


