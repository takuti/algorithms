import random

""" BOGOSORT

[algorithm]
1. Shuffle given data
2. The data is sorted?
  YES -> Finish
   NO -> Go step#1

[order]
O(n*n!) on average
"""

def sort(A, compare):
  def is_sorted():
    n = len(A)
    for i in range(n-1):
      if (not compare(A[i+1], A[i])) and (A[i+1] != A[i]): return False
    return True

  while not is_sorted():
    random.shuffle(A)
  return A
