""" QUICKSORT
"""

def partition(A, p, r):
  pivot = A[r]
  i = p - 1
  for j in range(p, r):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

def sort(A, p, r):
  """
  >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9)
  [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
  """
  if p < r:
    q = partition(A, p, r)
    sort(A, p, q-1)
    sort(A, q+1, r)
  return A

if __name__ == '__main__':
  import doctest
  doctest.testmod()
