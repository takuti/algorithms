""" SELECTION SORT

[algorithm]
  1: Select the minimum element from [1,n], and swap it for the first element
  2: Select the minimum element from [2,n], and swap it for the second element
     ...
n-1: Select the minimum element from [n-1,n], and swap it for the (n-1)-th element

[order]
O(n^2)
"""

def sort(A, compare):
  """
  [arguments]
  A -- Given array
  compare -- lambda function for comparison of two values (ascend or descend)

  [return]
  Sorted array
  """
  n = len(A)
  for i in range(n-1):
    selected_i = i
    for j in range(i, n):
      if compare(A[selected_i], A[j]): selected_i = j
    A[i], A[selected_i] = A[selected_i], A[i]
  return A
