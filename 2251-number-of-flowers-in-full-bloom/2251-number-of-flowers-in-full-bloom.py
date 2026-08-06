class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        s=sorted(start for start,end in flowers)
        e=sorted(end for start,end in flowers)
        ans=[]
        for p in people:
            started=bisect_right(s,p)
            ends=bisect_left(e,p)
            ans.append(started-ends)
        return ans
            