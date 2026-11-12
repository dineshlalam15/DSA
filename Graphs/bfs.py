from collections import deque

matrix = [[1,2],[0,2],[0,1,3,4],[2],[2]]

"""
Graph Structure based on the matrix. 
Iterate via index 
0 - branches to 1,2 
1 - branches to 0,2 
2 - branches to 0,1,3,4
3 - branches to 2
4 - branches to 2

Performing Breadth First Search (BFS) on the graph (undirected) & also continous
1. Visit 0 - Print 0
2. 1,2 are linked to 0, so visit 1 and then 2 - Print 1 & 2
3. Go to 1, neighbours of 1 are 0 & 2 - Both are already printed so avoid. 
4. Go to 2, neighbours are 0,1,3,4 - 0 & 1 are already printed. So avoid, and go to 3,4. 
5. Print 3 & 4
6. Check neighbours of 3 - 2 is already printed. 
7. Check neighbours of 4 - 2 is already printed. 
"""


class bfs:
    
    @staticmethod
    def bfs_connected_graph(matrix):
        v = len(matrix)
        visited = [False]*v
        res = []
        source = 0
        queue = deque()
        visited[source] = True
        queue.append(source)
        while queue:
            current = queue.popleft()
            res.append(current)
            for element in matrix[current]: 
                if not visited[element]:
                    visited[element] = True
                    queue.append(element)
        return res

    @staticmethod
    def connected(arr, source, visited, result):
        dq = deque()
        visited[source] = True
        dq.append(source)
        while dq: 
            current_node = dq.popleft()
            result.append(current_node)
            for element in arr[current_node]:
                if visited[element] is False: 
                    visited[element] = True
                    dq.append(element) 
                    
    @staticmethod
    def bfs_disconnected_graph(arr): 
        """
        In a disconnected graph, some vertices may not be reachable from a single source. 
        To ensure all vertices are visited in BFS traversal, 
        we iterate through each vertex, and if any vertex is unvisited, 
        we perform a BFS starting from that vertex being the source.
        """
        
        vertices = len(arr)
        visited = [False]*vertices
        result = []
        for idx in range(vertices):
            if visited[idx] is False:
                bfs.connected(arr, idx, visited, result)
        return result
    
if __name__ == "__main__": 
    print(bfs.bfs_connected_graph(matrix))
    arr = [[2, 3], [2], [0, 1], [0], [5], [4]]
    print(bfs.bfs_disconnected_graph(arr))