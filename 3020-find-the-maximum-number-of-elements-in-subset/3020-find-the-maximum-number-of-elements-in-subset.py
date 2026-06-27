class Solution(object):
    def maximumLength(self, nums):
        from collections import Counter
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = Counter(nums)
        ans = 1
        for key in mp:
            if key == 1:continue
            cur = key
            cnt = 0
            while cur in mp and mp[cur]>1:
                cnt+=2
                cur*=cur
            if cur not in mp:
                cnt-=1
            else:
                cnt+=1
            ans = max(ans, cnt)
        temp=mp.get(1, 0)
        if temp % 2 == 0:
            temp-= 1

        ans = max(ans,temp)
        return ans
            