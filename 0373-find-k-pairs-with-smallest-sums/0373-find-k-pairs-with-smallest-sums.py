class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans=[]
        if not nums1 or not nums2:
            return None
        seen=set()
        heap=[]
        heapq.heappush(heap,(nums1[0]+nums2[0],0,0))
        seen.add((0,0))
        while  heap and len(ans)<k:
            s,i,j=heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if i+1<len(nums1):
                i+=1
                if not (i,j) in seen:
                    seen.add((i,j))
                    heapq.heappush(heap,(nums1[i]+nums2[j],i,j))
                i-=1
            if j+1<len(nums2):
                j+=1
                if not (i,j) in seen:
                    seen.add((i,j))
                    heapq.heappush(heap,(nums1[i]+nums2[j],i,j))
        return ans



        