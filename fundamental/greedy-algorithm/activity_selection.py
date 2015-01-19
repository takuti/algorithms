""" activity-selection problem
find optimal solution such that maximize the number of activities
"""

def recursive_activity_selection(s, f, k, n):
  m = k + 1
  while m < n and s[m] < f[k]:
    m += 1
  if m == n: return []
  return [m] + recursive_activity_selection(s, f, m, n)

def greedy_activity_selector(s, f):
  n = len(s)
  A = [0]
  k = 1
  for m in range(1, n):
    if s[m] >= f[k]:
      A += [m]
      k = m
  return A

if __name__ == '__main__':
  s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
  f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
  print [0] + recursive_activity_selection(s, f, 0, len(s))
  print greedy_activity_selector(s, f)
