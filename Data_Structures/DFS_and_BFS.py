'''
Depth-first search and Breadth-first search
'''

# represent weights with nodes ds
# profit is a positive int, representing potential profit of a site
# name is a string representing the name of the node (for easy visualization)
class Node:
    def __init__(self, profit, name= None):
        self.name = name
        self.profit = profit
    
    def get_profit(self):
        return self.profit
    def get_name(self):
        return self.name

A = Node(1000,'A')
B = Node(800, 'B')
C = Node(350, 'C')
D = Node(400, 'D')
E = Node(1300, 'E')
F = Node(200, 'F')
G = Node(700, 'G')
H = Node(1400, 'H')
I = Node(2900, 'I')
J = Node(300, 'J')
K = Node(850, 'K')

# graph is a dictionary of Node object pointers
graph = {A:[C, D], B:[C], C:[A, B, F, G], D:[A, E],
 E:[D, H], F:[C, I], G: [C], H:[E, K], I:[F], J:[K], K:[H,J]}

'''
DEPTH FIRST SEARCH
'''
# visited is an array of previously explored nodes
# graph is a dict of adjacency lists (represents undir graph)
# node is node object
def DFS(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            DFS(visited, graph, neighbor)
    return visited

'''
BREADTH FIRST SEARCH
'''
def BFS(graph, node):
    visited = []
    queue= []
    visited.append(node)
    queue.append(node)
    while queue:
        to_vis = queue.pop(0)
        for neighbor in graph[to_vis]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return visited

def print_path(path):
    for node in path[:-1]:
        print(node.get_name(), end=" --> ")
    print(path[-1].get_name())

def path_weight(visited):
    sum = 0
    for node in visited:
        sum += node.get_profit()
    return sum

node = A 
visited= []
print_path(DFS(visited, graph, node))
print_path(BFS(graph, node))