# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        from collections import deque
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """
        if depth==1:
            new_r=TreeNode(val)
            new_r.left=root
            return new_r
        level=1
        q=deque([(root,level)])
        prev=None
        
        while q:
            size=len(q)
            for _ in  range(size):
                curr,lev=q.popleft()
                if lev==depth-1:
                    left_ch = curr.left
                    right_ch = curr.right

                    newn = TreeNode(val)
                    curr.left = newn
                    newn.left = left_ch

                    newn = TreeNode(val)
                    curr.right = newn
                    newn.right = right_ch
                else:
                    if curr.left:q.append((curr.left,lev+1))
                    if curr.right:q.append((curr.right,lev+1))
        return root
            



        