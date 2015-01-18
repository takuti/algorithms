""" bidirectional connected-list
head: sentinel cell
"""

class Cell:
  def __init__(self, x, prv=None, nxt=None):
    self.key = x
    self.prv = prv
    self.nxt = nxt

class List:
  def __init__(self):
    self.head = Cell(None)
    self.head.prv = self.head
    self.head.nxt = self.head

  def insert(self, x):
    x.nxt = self.head.nxt
    self.head.nxt.prv = x
    self.head.nxt = x
    x.prv = self.head

  def search(self, k):
    x = self.head.nxt
    while x != self.head and x.key != k:
      x = x.nxt
    return x

  def delete(self, x):
    x.prv.nxt = x.nxt
    x.nxt.prv = x.prv

  def __str__(self):
    x = self.head.nxt
    keys = []
    while x != self.head:
      keys.append(x.key)
      x = x.nxt
    return str(keys)

if __name__ == '__main__':
  l = List()
  print l # [] (empty)
  l.insert(Cell(1))
  l.insert(Cell(2))
  l.insert(Cell(3))
  print l # [3, 2, 1]
  x = l.search(2)
  l.delete(x)
  print l # [3, 1]
