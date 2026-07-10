class Solution(object):
    def validPath(self, n, edges, source, destination):
        from collections import defaultdict
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source==destination:return True
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen=set()

        stack=[source]
        while stack:
            curr=stack.pop()
            if curr==destination:return True
            for adj_ver in graph[curr]:
                if not adj_ver in seen:
                    seen.add(adj_ver)
                    stack.append(adj_ver) 
        return False



        