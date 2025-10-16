class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a, b):
            return len(set(a) & set(b))
        
        n = len(properties)
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False] * n
        components = 0
        
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components