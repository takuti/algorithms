# coding: utf-8

""" longest-common-subsequence (LCS) problem
d: ↖
u: ↑
l: ←
"""

lcs = []

def lcs_length(X, Y):
  m = len(X)
  n = len(Y)
  b = [0] * m
  for i in range(m):
    b[i] = [0] * n
  c = [0] * (m+1)
  for i in range(m+1):
    c[i] = [0] * (n+1)
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
        b[i-1][j-1] = 'd'
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        b[i-1][j-1] = 'u'
      else:
        c[i][j] = c[i][j-1]
        b[i-1][j-1] = 'l'
  return c, b

def get_lcs(b, X, i, j):
  if i == 0 or j == 0:
    return
  if b[i-1][j-1] == 'd':
    get_lcs(b, X, i-1, j-1)
    lcs.append(X[i-1])
  elif b[i-1][j-1] == 'u':
    get_lcs(b, X, i-1, j)
  else:
    get_lcs(b, X, i, j-1)

if __name__ == '__main__':
  X = 'ABCBDAB'
  Y = 'BDCABA'
  c, b = lcs_length(X, Y)
  get_lcs(b, X, len(X), len(Y))
  print ''.join(lcs)

