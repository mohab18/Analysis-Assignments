from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited, parent, cycle, start_vertex):
        visited[v] = True
        cycle.append(v);

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited, v, cycle, start_vertex)
            elif parent is not None and parent != neighbor:
               
                index = cycle.index(neighbor)
                if cycle[index] == start_vertex:
                    print("Cycle:", cycle[index:])
        
    def dfs(self, start, order='left'):
        visited = {node: False for node in self.graph}
        cycle = []

        self.dfs_util(start, visited, None, cycle, start)

    def bfs(self, start, order='left'):
        visited = {node: False for node in self.graph}
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in sorted(self.graph[node]):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def is_bipartite(self, start=1):
        visited = {node: False for node in self.graph}
        colors = {node: None for node in self.graph}
        queue = deque([start])
        colors[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in self.graph[node]:
                if colors[neighbor] is None:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False  

        return True  


g = Graph()
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 2)

print("DFS:")
g.dfs(1)
print("\nBFS:")
g.bfs(1)
print("\nIs Bipartite:", g.is_bipartite(1))
