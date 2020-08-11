from collections import defaultdict
import math

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # Function to print a BFS of graph

    def BFS(self, s,list):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            list.append(s)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
def ret_neighbors(maze,cell_id,N):
    x = int(math.floor(cell_id/N))
    y = cell_id-(x*N)
    list = []
    if (x > 0) and (maze[x - 1][y] == 1):
        list.append(cell_id-N)
    if (x < N-1) and (maze[x + 1][y] == 1):
        list.append(cell_id+N)
    if (y > 0) and (maze[x][y - 1] == 1):
        list.append(cell_id-1)
    if (y < N-1) and (maze[x][y + 1] == 1):
        list.append(cell_id+1)
    return list

N = int(input())
maze = [[0]*N for i in range(N)]
g = Graph()
counter = 0
found = False
answer = -1
g.addEdge(-1,-2)
g.addEdge(-1,-2)
while(1):
    bfs_list = []
    current = input()
    if(current == '-1'):
        break
    input_list = (current.split(" "))
    counter += 1
    x = int(input_list[0])
    y = int(input_list[1])
    cell_id = ((x-1)*N) + y-1
    maze[x-1][y-1] = 1
    if(x == 1):
        g.addEdge(-1,cell_id)
        g.addEdge(cell_id,-1)
    list_of_neighbors = ret_neighbors(maze, cell_id, N)
    for i in list_of_neighbors:
        g.addEdge(cell_id, int(i))
        g.addEdge(int(i), cell_id)
    g.BFS(-1,bfs_list)
    print(bfs_list)
    for j in bfs_list:
        if(int(j) >= (N * (N - 1))):
            found = True
            answer = counter
            break
    if(found == True):
        break
while(answer != -1):
    current = input()
    if(current == '-1'):
        break
print(answer)

