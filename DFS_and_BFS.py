'''
Depth-first search and Breadth-first search
'''
import time
from re import L
from Data_Structures import stacks_and_queues as sq
# represent weights with vertexs ds
# profit is a positive int, representing potential profit of a site
# name is a string representing the name of the vertex (for easy visualization)
class Vertex:
    def __init__(self, profit, name= None):
        self.name = name
        self.profit = profit
    
    def get_profit(self):
        return self.profit
    def get_name(self):
        return self.name

A = Vertex(1000,'A')
B = Vertex(800, 'B')
C = Vertex(350, 'C')
D = Vertex(400, 'D')
E = Vertex(1300, 'E')
F = Vertex(200, 'F')
G = Vertex(700, 'G')
H = Vertex(1400, 'H')
I = Vertex(2900, 'I')
J = Vertex(300, 'J')
K = Vertex(850, 'K')

# graph is a dictionary of vertex object pointers
graph = {A:[C, D], B:[C], C:[A, B, F, G], D:[A, E],
 E:[D, H], F:[C, I], G: [C], H:[E, K], I:[F], J:[K], K:[H,J]}

'''
DEPTH FIRST SEARCH
'''
# visited is an array of previously explored vertexs
# graph is a dict of adjacency lists (represents undir graph)
# vertex object
def DFS(graph, vertex):
    visited = []
    stack = sq.Stack()
    stack.push(vertex)
    while not stack.isEmpty():
        to_visit = stack.pop()
        if to_visit not in visited:
            visited.append(to_visit)
            for neighbor in graph[to_visit]:
                if neighbor not in visited:
                    stack.push(neighbor)
    return visited

'''
BREADTH FIRST SEARCH
'''
def BFS(graph, vertex):
    visited = []
    queue= sq.Queue()
    visited.append(vertex)
    queue.enqueue(vertex)
    while queue:
        to_vis = queue.dequeue()
        for neighbor in graph[to_vis]:
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.append(neighbor)
    return visited

def print_path(path):
    for vertex in path[:-1]:
        print(vertex.get_name(), end="  ")
    print(path[-1].get_name())
    return path

def path_weight(visited):
    sum = 0
    for vertex in visited:
        sum += vertex.get_profit()
    return sum

def mod_DFS(graph, vertex):
    visited = []
    skip = []
    stack = sq.Stack()
    stack.push(vertex)
    while stack.getSize() > 0:
        to_visit = stack.pop()
        if to_visit in visited or to_visit in skip:
            continue
        elif to_visit not in skip:
            visited.append(to_visit)
            for neighbor in graph[to_visit]:
                if neighbor not in visited and neighbor not in skip:
                    skip.append(neighbor)
                if neighbor in skip:
                    for n in graph[neighbor]:
                        if n not in visited and n not in skip:
                            stack.push(n)
    return visited

store_graph = [{'vertex': vertex, 'name': vertex.get_name(), 'profit': vertex.get_profit()} 
    for vertex in graph.keys()]
def sort_vertex(graph):
    return graph['profit']
store_graph.sort(key=sort_vertex, reverse=True)
final_graph = []
for dict in store_graph:
    final_graph.append(dict['vertex'])

'''
we want to memoize paths that have already been explored via DFS

'''
vis = []

stringpath = ''
weight = 0
st = time.time()
for vertex in final_graph:
    stringpath += vertex.get_name() + "  "
    weight += vertex.get_profit()
end = time.time()
elapsed = end-st
print(stringpath, weight, elapsed, sep = "  ")

for vertex in final_graph:
    if vertex not in vis:
        st = time.time()
        path = mod_DFS(graph, vertex)
        end = time.time()
        elapsed = end-st
        weight = path_weight(path)
        vis.extend(path)
        print_path(path)
        print(weight, "Time: ", elapsed)
        

        