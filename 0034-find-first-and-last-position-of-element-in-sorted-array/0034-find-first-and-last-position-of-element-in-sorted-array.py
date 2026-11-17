class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def boundary(isLeft):
            l,r=0,len(nums)-1
            ans=-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    if isLeft:
                        r=mid-1
                    else:
                        l=mid+1

                elif nums[mid] < target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        left=boundary(True)
        right=boundary(False)
        return [left,right]

 