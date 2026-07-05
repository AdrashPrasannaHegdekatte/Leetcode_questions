class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

    
        sheap=[]
        lheap=[]
        delayed=defaultdict(int)
        ss=0
        ls=0
        l=0
        def prune(heap):
            while heap:
                if heap is sheap:
                    num=-heap[0]
                else:
                    num=heap[0]
                if delayed[num]:
                    heapq.heappop(heap)
                    delayed[num]-=1
                    if delayed[num]==0:
                        del delayed[num]
                else:
                    break
        def rebalance():
            nonlocal ss,ls
            if ss>ls+1:
                num=-heapq.heappop(sheap)
                heapq.heappush(lheap,num)
                ss-=1
                ls+=1
                prune(sheap)
            elif ss<ls:
                num=heapq.heappop(lheap)
                heapq.heappush(sheap,-num)
                ls-=1
                ss+=1
                prune(lheap)
        def add(num):
            nonlocal ss,ls
            if not sheap or num<=-sheap[0]:
                heapq.heappush(sheap,-num)
                ss+=1
            else:
                heapq.heappush(lheap,num)
                ls+=1
            rebalance()
        def remove(num):
            nonlocal ss,ls
            delayed[num]+=1
            if num<= -sheap[0]:
                ss-=1
                if num== -sheap[0]:
                    prune(sheap)
            else:
                ls-=1
                if num==lheap[0]:
                    prune(lheap)
            rebalance()

        def getMedian():
            prune(sheap)
            prune(lheap)
            if k%2:
                return float(-sheap[0])
            return (-sheap[0]+lheap[0])/2.0
        for r in range(k):
            add(nums[r])
        ans=[getMedian()]
        for i in range(k,len(nums)):
            remove(nums[i-k])
            add(nums[i])
            ans.append(getMedian())
        return ans
        
        