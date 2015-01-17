""" RADIXSORT
"""

def counting_sort(S, A, k):
  """ sort S besed on the result of counting-sort for A
  """
  C = [0] * k
  n = len(A)
  for j in range(n):
    C[A[j]] += 1
  for i in range(1, k):
    C[i] += C[i-1]
  B = [0] * n
  for j in range(n-1,-1,-1):
    B[C[A[j]]-1] = S[j]
    C[A[j]] -= 1
  return B

def sort(A, d):
  """ Each element has d-digits
  >>> sort([329,457,657,839,436,720,355], 3)
  [329, 355, 436, 457, 657, 720, 839]
  """
  for i in range(0, d):
    digits = [int(str(v)[d-1-i]) for v in A]
    A = counting_sort(A, digits, max(digits)+1)
  return A

if __name__ == '__main__':
  import doctest
  doctest.testmod()
