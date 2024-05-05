class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist, path):
        print("Vertex \t Distance from Source \t Path")
        for node in range(self.V):
            print(f"X{node+1} \t\t{dist[node]} \t\t", end='')
            for x in path[node]:
                print(f'X{x+1}', end='-')
            print(f'X{node+1}')

    def minDistance(self, dist, sptSet):
        min = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self):
        dist = [float('inf')] * self.V
        path = [[] for _ in range(self.V)]
        dist[0] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    path[v] = path[u] + [u]

        self.printSolution(dist, path)


if __name__ == '__main__':
    g = Graph(13)
    g.graph = [[0, 5, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
               [5, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
               [3, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0],
               [2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
               [3, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
               [0, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
               [0, 2, 0, 1, 2, 0, 0, 0, 0, 2, 0, 2, 0],
               [0, 0, 3, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 4],
               [0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 4],
               [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 4],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 0]]

    g.dijkstra()
