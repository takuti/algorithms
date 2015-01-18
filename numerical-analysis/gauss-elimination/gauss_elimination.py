import numpy as np

def solve(A, b):
  n = np.shape(A)[0]

  # Forward elimination
  for j in range(n-1):
    for i in range(j+1, n):
      b[i] -= (b[j] / A[j][j] * A[i][j])
      for k in range(j+1, n):
        A[i][k] -= (A[j][k] / A[j][j] * A[i][j])
      A[i][j] = 0

  x = np.zeros([n])
  # Back substitution
  for i in range(n-1, -1, -1):
    x[i] = b[i] / A[i][i]
    for j in range(i+1, n):
      x[i] -= (A[i][j] * x[j]) / A[i][i]
  return x

if __name__ == '__main__':
  A = np.array([[1, 2, 3, 4],
                [2, 2, 3, 4],
                [3, 3, 3, 4],
                [4, 4, 4, 4]], dtype='float64')
  b = np.array([1.234, 2.234, 3.334, 4.444], dtype='float64')

  print solve(A, b)
