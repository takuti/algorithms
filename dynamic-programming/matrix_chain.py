""" matrix-chain multiplication problem
Find the optimal matrix-chain multiplication order which minimize multiply-operations
"""

import sys

def matrix_chain_order(p):
  n = len(p) - 1
  m = [0] * n
  for i in range(n):
    m[i] = [0] * n
  s = [0] * (n-1)
  for i in range(n-1):
    s[i] = [0] * (n-1)

  for l in range(2, n+1):
    for i in range(1, n-l+1+1):
      j = i + l -1
      m[i-1][j-1] = float('inf')
      for k in range(i, j-1+1):
        q = m[i-1][k-1] + m[k+1-1][j-1] + p[i-1] * p[k] * p[j]
        if q < m[i-1][j-1]:
          m[i-1][j-1] = q
          s[i-1][j-2] = k
  return m, s

def print_optimal_parens(s, i, j):
  if i == j:
    sys.stdout.write('A%d' % i)
  else:
    sys.stdout.write('(')
    print_optimal_parens(s, i, s[i-1][j-2])
    print_optimal_parens(s, s[i-1][j-2]+1, j)
    sys.stdout.write(')')

if __name__ == '__main__':
  p = [30, 35, 15, 5, 10, 20, 25]
  m, s = matrix_chain_order(p)
  print_optimal_parens(s, 1, 6)
  print ''

