""" heap
maximum heap
- parent node is always greater than 2 children nodes
"""

def left(i):
  return 2 * i

def right(i):
  return 2 * i + 1

def max_heapify(A, size, i):
  l = left(i)
  r = right(i)

  largest = l if l < size and A[l] > A[i] else i
  largest = r if r < size and A[r] > A[largest] else largest
  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    max_heapify(A, size, largest)

def build_max_heap(A, size):
  n = size / 2
  for i in range(n-1,-1,-1):
    max_heapify(A, size, i)
