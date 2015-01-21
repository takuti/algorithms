""" Union-Find data-structure for disjoint-set
"""

class UF:
  def __init__(self, size):
    self.V = [i for i in range(size+1)] # list for all elements
    self.size = size
    for i in range(1, self.size+1):
      self.V[i] = i

  def __str__(self):
    return str(self.V)

  def union(self, u, v):
    s1 = self.V[u]
    s2 = self.V[v]
    for i in range(1, self.size+1):
      if self.V[i] == s2:
        self.V[i] = s1

  def find(self, u):
    return self.V[u]

if __name__ == '__main__':
  uf = UF(10)
  uf.union(2, 4)
  uf.union(5, 7)
  uf.union(1, 3)
  uf.union(8, 9)
  uf.union(1, 2)
  uf.union(5, 6)
  uf.union(2, 3)
  print uf # [1, 2, 3, 4] [5, 6, 7] [8, 9] [10]







