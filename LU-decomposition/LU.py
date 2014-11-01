import numpy as np

def decompose(A):
  n = np.shape(A)[0]
  LU = np.zeros([n,n])

  for i in range(n):
    LU[i][0] = A[i][0]

  # except for the diagonal element because it's always 1
  for j in range(1, n):
    LU[0][j] = A[0][j] / LU[0][0]

  for j in range(1, n):
    for i in range(j, n):
      s = 0
      for k in range(j):
        s += LU[i][k] * LU[k][j]
      LU[i][j] = A[i][j] - s
    for i in range(j+1, n):
      s = 0
      for k in range(j):
        s += LU[j][k] * LU[k][i]
      LU[j][i] = (A[j][i] - s) / LU[j][j]
  return LU

def solve(LU, b):
  n = np.shape(LU)[0]

  for i in range(n):
    s = 0
    for k in range(i):
      s += LU[i][k] * b[k]
    b[i] = (b[i] - s) / LU[i][i]

  x = np.zeros([n])
  x[n-1] = b[n-1]
  for j in range(n-2, -1, -1):
    s = 0
    for k in range(j+1, n):
      s += LU[j][k] * x[k]
    x[j] = b[j] - s

  return x

if __name__ == '__main__':
  A = np.array([[1, 2, 3, 4],
                [2, 2, 3, 4],
                [3, 3, 3, 4],
                [4, 4, 4, 4]], dtype='float64')
  b = np.array([1.234, 2.234, 3.334, 4.444], dtype='float64')

  print solve(decompose(A), b)

