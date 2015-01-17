""" QUICKSORT
"""

import random

def partition(A, p, r):
  pivot = A[r]
  i = p - 1
  for j in range(p, r):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

def randomized_partition(A, p, r):
  i = random.randint(p, r)
  A[i], A[r] = A[r], A[i]
  return partition(A, p, r)

def sort(A, p, r, randomize_flg=False):
  """
  >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9)
  [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
  >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 0, 9, True)
  [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
  """
  if p < r:
    q = randomized_partition(A, p, r) if randomize_flg else partition(A, p, r)
    sort(A, p, q-1)
    sort(A, q+1, r)
  return A

if __name__ == '__main__':
  import doctest
  doctest.testmod()
