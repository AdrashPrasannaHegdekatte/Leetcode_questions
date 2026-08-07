class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def num_sub(limit):
            s=0
            cnt=0
            for num in nums:
                s+=num
                if s>limit:
                    s=num
                    cnt+=1
            return cnt+1
        n=len(nums)
        l=max(nums)
        h=sum(nums)

        while(l<h):
            mid=l+(h-l)//2
            
            if num_sub(mid)>k:
                l=mid+1
            else:
                h=mid
        return l


        