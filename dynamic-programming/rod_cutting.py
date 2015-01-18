""" rod-cutting problem
- You have a rod, and the length is n.
- The rod-cutting problem is an optimization problem to maximize profit by cut-and-sell process.
- Which will cutting length and their order be the optimal solution?
- n and profit for each cut-rod length p[] are given.
"""

""" Recursive method
This way takes almost infinite time for a long rod.
"""
def cut_rod(p, n):
  if n == 0:
    return 0
  q = 0
  for i in range(1, n+1):
    q = max(q, p[i] + cut_rod(p, n-i))
  return q

""" Dynamic programming: top-down with memoization
"""
def memoized_cut_rod(p, n):
  """
  >>> memoized_cut_rod([0,1,5,8,9,10,17,17,20,24,30], 10)
  30
  """
  r = [-1] * (n+1)
  return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
  if r[n] >= 0: return r[n]
  if n == 0:
    q = 0
  else:
    q = -1
    for i in range(1, n+1):
      q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
  r[n] = q
  return q

""" Dynamic programming: bottom-up
"""
def bottom_up_cut_rod(p, n):
  """
  >>> bottom_up_cut_rod([0,1,5,8,9,10,17,17,20,24,30], 10)
  30
  """
  r = [-1] * (n+1)
  r[0] = 0
  for j in range(1, n+1):
    q = -1
    for i in range(1, j+1):
      q = max(q, p[i] + r[j-i])
    r[j] = q
  return r[n]

""" For printing results of the rod-cutting problem
Above solutions just return the optimal price. They do not provide cutting length.
"""
def extended_bottom_up_cut_rod(p, n):
  """
  >>> extended_bottom_up_cut_rod([0,1,5,8,9,10,17,17,20,24,30], 10)
  ([0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30], [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10])
  """
  r = [-1] * (n+1)
  s = [0] * (n+1)
  r[0] = 0
  for j in range(1, n+1):
    q = -1
    for i in range(1, j+1):
      if q < p[i] + r[j-i]:
        q = p[i] + r[j-i]
        s[j] = i
    r[j] = q
  return r, s

def print_cut_rod_solution(p, n):
  """
  >>> print_cut_rod_solution([0,1,5,8,9,10,17,17,20,24,30], 10)
  10
  >>> print_cut_rod_solution([0,1,5,8,9,10,17,17,20,24,30], 7)
  1
  6
  """
  r, s = extended_bottom_up_cut_rod(p, n)
  while n > 0:
    print s[n]
    n = n - s[n]

if __name__ == '__main__':
  import doctest
  doctest.testmod()

