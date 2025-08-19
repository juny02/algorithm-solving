

def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if i not in visited:
                visited[i] = True
                stack.add