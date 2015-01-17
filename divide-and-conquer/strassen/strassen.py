# coding: utf-8

def create_2dimensional_array(n):
  A = [0] * n
  for i in range(n):
    A[i] = [0] * n
  return A

def submatrix(A, i, j):
  """ Return (i, j) submatrix of 4-divided A
  >>> submatrix([[1,2,3,4],[5,6,7,8], [9,10,11,12],[13,14,15,16]], 0, 1)
  [[3, 4], [7, 8]]
  >>> submatrix([[3, 4], [7, 8]], 0, 1)
  [[4]]
  """
  n = len(A) / 2
  A_new = create_2dimensional_array(n)
  for k in range(n):
    for l in range(n):
      A_new[k][l] = A[n*i+k][n*j+l]
  return A_new

def add(A, B, sign=1):
  """ Add 2 arrays (A + B)
  if sign = -1, returns the result of (A - B)
  >>> add([[1,2],[3,4]], [[5,6],[7,8]])
  [[6, 8], [10, 12]]
  >>> add([[1,2],[3,4]], [[5,6],[7,8]], -1)
  [[-4, -4], [-4, -4]]
  """
  n = len(A)
  S = create_2dimensional_array(n)
  for i in range(n):
    for j in range(n):
      S[i][j] = A[i][j] + sign * B[i][j]
  return S

def multiply(A, B):
  """ Multiply 2 arrays (A * B) by Strassen's method
  >>> multiply([[1,2],[3,4]],[[5,6],[7,8]])
  [[19, 22], [43, 50]]
  """
  n = len(A)
  C = create_2dimensional_array(n)
  if n == 1:
    C[0][0] = A[0][0] * B[0][0]
  else:
    A11 = submatrix(A, 0, 0)
    A12 = submatrix(A, 0, 1)
    A21 = submatrix(A, 1, 0)
    A22 = submatrix(A, 1, 1)

    B11 = submatrix(B, 0, 0)
    B12 = submatrix(B, 0, 1)
    B21 = submatrix(B, 1, 0)
    B22 = submatrix(B, 1, 1)

    S1 = add(B12, B22, -1)
    S2 = add(A11, A12)
    S3 = add(A21, A22)
    S4 = add(B21, B11, -1)
    S5 = add(A11, A22)
    S6 = add(B11, B22)
    S7 = add(A12, A22, -1)
    S8 = add(B21, B22)
    S9 = add(A11, A21, -1)
    S10 = add(B11, B12)

    P1 = multiply(A11, S1)
    P2 = multiply(S2, B22)
    P3 = multiply(S3, B11)
    P4 = multiply(A22, S4)
    P5 = multiply(S5, S6)
    P6 = multiply(S7, S8)
    P7 = multiply(S9, S10)

    C11 = add(add(add(P5, P4), P2, -1), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = add(add(add(P5, P1), P3, -1), P7, -1)
    for i in range(n):
      for j in range(n):
        if i < n/2 and j < n/2:
          v = C11[i][j]
        elif i < n/2 and j >= n/2:
          v = C12[i][j-n/2]
        elif i >= n/2 and j < n/2:
          v = C21[i-n/2][j]
        else:
          v = C22[i-n/2][j-n/2]
        C[i][j] = v
  return C

if __name__ == '__main__':
  import doctest
  doctest.testmod()

