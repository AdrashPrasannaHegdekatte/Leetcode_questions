# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        from collections import deque
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:return []
        ans=[]
        q=deque([root])

        while q:
            level_size=len(q)
            max_elem=float("-inf")
            for i in range(level_size):
                curr=q.popleft()
                max_elem=max(max_elem,curr.val)
                if curr.left:q.append(curr.left)
                if curr.right:q.append(curr.right)
            ans.append(max_elem)
        return ans
            
        