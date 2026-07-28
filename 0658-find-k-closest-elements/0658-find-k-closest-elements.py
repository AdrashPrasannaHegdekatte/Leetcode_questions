class Solution(object):
    def findClosestElements(self, arr, k, x):
    
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n=len(arr)
        if x<arr[0]:return arr[0:k]
        if x>arr[-1]:return arr[-k:]
        def bs(arr,tar):
            l,r=0,len(arr)

            while(l<r):
                mid=l+(r-l)//2
                
                if arr[mid]>tar:
                    r=mid
                else:
                    l=mid+1
            return l
        ans=[]
        idx=bs(arr,x)
        
        if idx-1>=0: i=idx-1
        j=idx
    
        while k>0:
            if i<0:
                ans.append(arr[j])
                j+=1
                k-=1
                continue
            if j>n-1:
                ans.append(arr[i])
                i-=1
                k-=1
                continue
            elif arr[j]-x<x-arr[i]:
                ans.append(arr[j])
                j+=1
            else:
                ans.append(arr[i])
                i-=1
            k-=1

        ans.sort()
        return ans