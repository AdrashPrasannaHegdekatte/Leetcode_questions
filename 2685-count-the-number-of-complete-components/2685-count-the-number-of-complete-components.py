class Solution(object):
    def countCompleteComponents(self, n, edges):
        from collections import defaultdict
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen=set()
        c=0
        for node in range(n):
            if not node in seen:
                seen.add(node)
                stack=[node]
                ver=0
                ed=0
                while stack:
                    node=stack.pop()
                    ver+=1
                    ed+=len(graph[node])
                    for adj_ver in graph[node]:
                        if not adj_ver in seen:
                            seen.add(adj_ver)
                            stack.append(adj_ver)
                aed=ed//2
                if ((ver)*(ver-1))/2==aed:
                    c+=1
        return c

        
            

        