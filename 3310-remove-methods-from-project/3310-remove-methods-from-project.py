class Solution(object):
    def remainingMethods(self, n, k, invocations):
        from collections import deque,defaultdict
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        adj=defaultdict(list)
        for u,v in invocations:
            adj[u].append(v)
        vis=set()
        q=deque([k])
        vis.add(k)
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v in adj[u]:
                    if v not in vis:
                        vis.add(v)
                        q.append(v)
            
        for u,v in invocations:
            if u not in vis and v in vis:
                return list(range(n))
        return [i for i in range(n) if i not in vis]
        
        