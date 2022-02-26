'''
Depth-first search and Breadth-first search
'''

#represent weights with nodes ds
# profit is a positive int, representing potential profit of a site
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

def weight_sort(graph):
    weights = {nod.get_name():nod.get_profit() for nod in graph}
    by_weight = sorted(weights.items(), key=lambda x:x[1], reverse=True)   
    #Traverse list backwards because InsertionSort yields least to greatest and we want greatest to least
    sorted_weight_dict = {name: weight for (name, weight) in by_weight}
    return sorted_weight_dict

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

def print_path(path):
    for node in path[:-1]:
        print(node.get_name(), end="-->")
    print(path[-1].get_name())

def path_weight(visited):
    sum = 0
    for node in visited:
        sum += node.get_profit()
    return sum

node = A 
visited= []
DFS(visited, graph, node)
