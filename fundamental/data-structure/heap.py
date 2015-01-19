""" heap
maximum heap
- parent node is always greater than 2 children nodes
"""

class MaxHeap:
  def __init__(self, A):
    self.A = A
    self.size = len(A)
    build_max_heap()

  def left(self, i):
    return 2 * i

  def right(self, i):
    return 2 * i + 1

  def max_heapify(i):
    l = self.left(i)
    r = self.right(i)

    largest = l if l < self.size and self.A[l] > self.A[i] else i
    largest = r if r < self.size and self.A[r] > self.A[largest] else largest
    if largest != i:
      self.A[i], self.A[largest] = self.A[largest], self.A[i]
      self.max_heapify(largest)

  def build_max_heap():
    n = self.size / 2
    for i in range(n-1,-1,-1):
      self.max_heapify(i)
