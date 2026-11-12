"""
DFS - DEPTH FIRST SEARCH
Searching till the leaf node
"""

from collections import defaultdict
class dfs:
    
    @staticmethod
    def dfs_recursion(adj, visited, source, result):
        visited[source] = True
        result.append(source)
        for element in adj[source]:
            if not visited[element]:
                dfs.dfs_recursion(adj, visited, element, result)
            
    @staticmethod
    def backtrack(adj):
        length = len(adj)
        visited = [False] * length
        result = []
        source = 0
        dfs.dfs_recursion(adj, visited, source, result)
        return result

    @staticmethod
    def build_adj_list(edges, num_vertices=None, undirected=True):
        import pdb; pdb.set_trace()
        if not edges:
            return []
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            if undirected:
                adj[v].append(u)
        return adj


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]]
    converted_adj = dfs.build_adj_list(edges)
    print("DFS (from Edge List):", dfs.backtrack(converted_adj))