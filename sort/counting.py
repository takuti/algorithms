""" COUNTINGSORT
1) count frequency of each value
2) generate sorted-list
"""

def sort(A, k):
  """ values are selected in [0, k]
  >>> sort([43, 2, 15, 81, 49, 4, 56, 11, 51, 97], 100)
  [2, 4, 11, 15, 43, 49, 51, 56, 81, 97]
  """
  C = [0] * k
  n = len(A)
  for j in range(n):
    C[A[j]] += 1
  for i in range(1, k):
    C[i] += C[i-1]
  B = [0] * n
  for j in range(n-1,-1,-1):
    B[C[A[j]]-1] = A[j]
    C[A[j]] -= 1
  return B

if __name__ == '__main__':
  import doctest
  doctest.testmod()

