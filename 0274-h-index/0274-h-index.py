class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h_ind=0
        for i in range(len(citations)-1,-1,-1):
            if citations[i]>h_ind:
                h_ind+=1
        return h_ind
