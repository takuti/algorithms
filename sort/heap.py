""" HEAPSORT
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

def sort(A):
  """
  >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97])
  [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
  """
  n = len(A)
  build_max_heap(A, n)
  for i in range(n-1,0,-1):
    A[0], A[i] = A[i], A[0]
    n -= 1
    max_heapify(A, n, 0)
  return A

if __name__ == '__main__':
  import doctest
  doctest.testmod()

