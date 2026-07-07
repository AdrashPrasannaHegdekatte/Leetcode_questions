# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap=[]
        if not lists:
            return None
        dummy=ListNode(-1)
        for l in lists:
            if l:
                heapq.heappush(heap,(l.val,l))
        if not heap:
            return None
        k=len(lists)
        s,head=heapq.heappop(heap)
        dummy.next=head
        curr=head
        if head.next:
            heapq.heappush(heap,(head.next.val,head.next))
        else:
            k-=1
        while(k>1):
            if heap:
                v,m=heapq.heappop(heap)
                curr.next=m
                curr=m
                if m.next:
                    heapq.heappush(heap,(m.next.val,m.next))
                else:
                    k-=1
            else:
                break
        if heap:
            _,m=heapq.heappop(heap)
            curr.next=m
        return dummy.next
