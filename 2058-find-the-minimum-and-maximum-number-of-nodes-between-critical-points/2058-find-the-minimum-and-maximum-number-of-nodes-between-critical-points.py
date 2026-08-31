# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev=head
        curr=head.next
        pos=1

        f=-1
        l=-1
        minDist=float("inf")

        while curr.next:
            nxt=curr.next

            if ((curr.val>prev.val and curr.val>nxt.val) or
                (curr.val<prev.val and curr.val<nxt.val)):

                if f==-1:
                    f=pos
                else:
                    minDist=min(minDist,pos-l)

                l=pos

            prev=curr
            curr=nxt
            pos+=1

        if f==l:
            return [-1, -1]

        return [minDist,l-f]