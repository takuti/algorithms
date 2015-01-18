""" hash
"""

import connected_list as L

class ChainedHash:
  """ Chained Hash using connected-list
  hash functions
  - int(k * m) if 0 <= k <= 1
  - k % m
  - int(m * ((k * A) % 1)) for 0 < A < 1
  """
  def __init__(self, h, size=10):
    self.T = []
    for i in range(size):
      self.T.append(L.List())
    self.h = h

  def __str__(self):
    s = ''
    n = len(self.T)
    for i in range(n):
      s += 'hashed-value#%d = %s\n' % (i, str(self.T[i]))
    return s

  def search(self, k):
    return self.T[self.h(k)].search(k)

  def insert(self, k, x):
    self.T[self.h(k)].insert(x)

  def delete(self, k, x):
    self.T[self.h(k)].delete(x)

class DirectAdressing:
  """ The simplest way: Direct Addressing (just use an array)
  """
  def __init__(self, size=10):
    self.T = [None] * size

  def search(self, k):
    return self.T[k]

  def insert(self, k, v):
    self.T[k] = v

  def delete(self, k):
    self.T[k] = None

class OpenAddressing:
  """ Memorize all elements in a hash table
  hash functions to generate [0, m-1]
  - linear probing:    h(k, i) = (h'(k) + 1) % m
  - quadratic probing: h(k, i) = (h'(k) + c1 * i + c2 * i**2) % m
  - double hashing:    h(k, i) = (h1(k) + i * h2(k)) % m
  double hashing is one of the best hash functions
  """
  def __init__(self, h, size=10):
    self.T = [None] * size
    self.h = h

  def search(self, k):
    i = 0
    m = len(self.T)
    while True:
      j = self.h(k, i)
      if self.T[j] == k:
        return j
      i += 1
      if T[j] == None or i == m: break

  def insert(self, k):
    i = 0
    m = len(self.T)
    while True:
      j = self.h(k, i)
      if self.T[j] == None:
        T[j] = k
        return j
      else:
        i += 1
      if i == m: break

if __name__ == '__main__':
  ch = ChainedHash(lambda k: k % 5, 5)
  for k in [10, 11, 12, 13, 20, 12, 32]:
    ch.insert(k, L.Cell(k))
    print ch
