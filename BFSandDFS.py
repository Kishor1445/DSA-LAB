from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, start):
        visited = [False] * len(self.graph)
        queue = [start]
        visited[start] = True
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for i in self.graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()
    
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    
    def DFS(self):
        V = len(self.graph)
        visited = [False]* (V)
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("BFS:")
g.BFS(2)
print("DFS:")
g.DFS()
