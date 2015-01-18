""" binary-search-tree
"""

class Node:
  def __init__(self, k, l=None, r=None, p=None):
    self.key = k
    self.l = l
    self.r = r
    self.p = p

class Tree:
  def __init__(self):
    self.root = None

  def walk(self, x):
    if x != None:
      self.walk(x.l)
      print x.key
      self.walk(x.r)

  def insert(self, z):
    y = None
    x = self.root
    while x != None:
      y = x
      x = x.l if z.key < x.key else x.r
    z.p = y
    if y == None:
      self.root = z # z is the first node
    elif z.key < y.key:
      y.l = z
    else:
      y.r = z

  def search(self, x, k):
    while x != None and x.key != k:
      x = x.l if k < x.key else x.r
    return x

  def minimum(self, x):
    while x.l != None:
      x = x.l
    return x

  def maximum(self, x):
    while x.r != None:
      x = x.r
    return x

  def successor(self, x):
    """ return node which will be printed next to x in walk()
    """
    if x.r != None:
      return self.minimum(x.r)
    y = x.p
    while y != None and x == y.r:
      x = y
      y = y.p
    return y

  def transplant(self, u, v):
    """ replace root from u to v
    """
    if u.p == None:
      self.root = v
    elif u == u.p.l:
      u.p.l = v
    else:
      u.p.r = v
    if v != None:
      v.p = u.p

  def delete(self, z):
    if z.l == None:
      self.transplant(z, z.r)
    elif z.r == None:
      self.transplant(z, z.l)
    else:
      y = self.minimum(z.r)
      if y.p != z:
        self.transplant(y, y.r)
        y.r = z.r
        y.r.p = y
      self.transplant(z, y)
      y.l = z.l
      y.l.p = y

if __name__ == '__main__':
  import random
  T = Tree()
  l = [random.randint(1, 100) for i in range(10)]
  print l
  for k in l:
    T.insert(Node(k))
  T.walk(T.root)
  print '---'
  x = T.successor(T.search(T.root, l[5]))
  if x == None: print '%d is the last.' % l[5]
  else: print 'next to %d is %d' % (l[5], x.key)
  print '---'
  for k in l:
    T.delete(T.search(T.root, k))
  T.walk(T.root)


