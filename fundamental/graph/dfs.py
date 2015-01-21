""" Depth-first search
"""

WHITE = -1
GRAY = 0
BLACK = 1

class Node:
  def __init__(self, color=WHITE, pi=None, d=0, f=0):
    self.color = color
    self.pi = pi
    self.d = d
    self.f = f
    self.adj = []

class Graph:
  """ Create a graph G(V, E)
  V is a set of vertices such as {a, b, c, d, ...}
  E is an edge list. One element (a, b) indicates a connection from node-a to node-b
  """
  def __init__(self, V, E):
    self.V = {}
    for vertex in V:
      self.V[vertex] = Node()
    for n1, n2 in E:
      self.V[n1].adj.append(self.V[n2])

time = 0

def dfs(G):
  global time
  time = 0
  for k, u in G.V.items():
    if u.color == WHITE:
      dfs_visit(G, u)

def dfs_visit(G, u):
  global time
  time += 1
  u.d = time
  u.color = GRAY
  for v in u.adj:
    if v.color == WHITE:
      v.pi = u
      dfs_visit(G, v)
  u.color = BLACK
  time += 1
  u.f = time

if __name__ == '__main__':
  V = ['u', 'v', 'w', 'x', 'y', 'z']
  E = [('u', 'v'), ('u', 'x'), ('x', 'v'), ('v', 'y'), ('y', 'x'), ('w', 'y'), ('w', 'z'), ('z', 'z')]
  G = Graph(V, E)
  dfs(G)
  for vertex in V:
    print '%c: %d/%d' % (vertex, G.V[vertex].d, G.V[vertex].f)

