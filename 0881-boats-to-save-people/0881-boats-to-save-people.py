class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        if people[0]>limit:return 0
        people.sort()
        l=0
        cnt=0
        r=len(people)-1
        while(l<=r):
            cnt+=1
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
        return cnt

