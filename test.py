
class Vertex:
    def __init__(self, val, name=None):
        self.value = val
        self.visited = False
        self.pi = None
        self.name = name

class Graph:
    def __init__(self):
        self.vertices = []
        self.adj = {}

def DFS(G):
    for v in G.vertices:
        if not(v.visited):
            DFS_Visit(G, v)
    return True

def DFS_Visit(G, v):
    v.visited = True
    for u in G.adj[v]:
        if not(u.visited):
            u.pi = v
            DFS_Visit(G, u)
    return True

gr = Graph()
A = Vertex(1, 'A')
B = Vertex(2, 'B')
C = Vertex(3, 'C')
D = Vertex(4, 'D')
E = Vertex(5, 'E')
F = Vertex(7, 'F')
G = Vertex(6, 'G')
H = Vertex(10, 'H')
I = Vertex(8, 'I')
J = Vertex(3, 'J')
K = Vertex(0, 'K')
verts = [A, B, C, D, E, F, G, H, I, J, K]
for ver in verts:
    gr.vertices.append(ver)
gr.adj = {A: [C, D], B: [C], C: [A, B, F, G], D: [A, E], E: [D, H],
F: [C, I], G: [C], H: [E, K], I: [E], J: [K], K: [H, J]}
DFS(gr)
for v in gr.vertices:
    if v.pi:
        print(v.name, v.pi.name)
    if v.pi is None:
        print(v.name, "is the root")